import mongoose from "mongoose";
import Provider from "./models/provider.js";
import Detail from "./models/detail.js";
import PriceHistory from "./models/price-history.js";

async function seed() {
  await mongoose.connect("mongodb://127.0.0.1:27017/autoparts");
  console.log("DB connected");

  // Очистка коллекций
  await Provider.deleteMany({});
  await Detail.deleteMany({});
  await PriceHistory.deleteMany({});

  // --- 5 валидных провайдеров ---
  const providersData = [
    { name: "ТехПром", address: "Минск, Ленина 10", phone: "+375291111111" },
    { name: "ДетальСервис", address: "Минск, Немига 25", phone: "+375292222222" },
    { name: "ПромМет", address: "Гомель, Советская 50", phone: "+375293333333" },
    { name: "МехИндустрия", address: "Витебск, Мира 14", phone: "+375294444444" },
    { name: "УралПоставка", address: "Брест, Советская 7", phone: "+375295555555" }
  ];

  const providers = await Provider.insertMany(providersData);
  console.log("Providers created");

  // --- 15 валидных деталей ---
  const detailsNames = [
    "Болт М6","Гайка М6","Шайба 6мм","Подшипник 6000","Шестерня малая",
    "Шестерня большая","Ремень приводной","Муфта соединительная","Фильтр масляный",
    "Фильтр воздушный","Втулка опорная","Штифт фиксирующий","Вал приводной",
    "Кронштейн крепления","Прокладка резиновая"
  ];

  for (let i = 0; i < detailsNames.length; i++) {
    const detailName = detailsNames[i];
    const article = `ART-${1000 + i}`;

    // 1–3 случайных провайдера для детали
    const count = Math.floor(Math.random() * 3) + 1;
    const randomProviders = providers.sort(() => 0.5 - Math.random()).slice(0, count);

    // создаём деталь
    const detail = await Detail.create({
      name: detailName,
      article,
      providers: randomProviders.map(p => p._id)
    });

    // создаём PriceHistory с первой ценой > 0
    const priceHistory = await PriceHistory.create({
      detailId: detail._id,
      history: [
        { price: Math.floor(Math.random() * 500) + 50 } // 50–550
      ]
    });

    detail.priceHistory = priceHistory._id;
    await detail.save();
  }

  console.log("Details and PriceHistory created");
  mongoose.connection.close();
  console.log("DB seeding completed");
}

seed().catch(err => console.error(err));
