import express from 'express';
import mongoose from 'mongoose';
import session from 'express-session';
import * as DetailController from './controllers/DetailController.js';
import * as ProviderController from './controllers/ProviderController.js';
import * as OrderController from './controllers/OrderController.js';
import * as DetectController from './controllers/DetectController.js';
import passport from './passport.js';
import checkAuth from './middleware/checkAuth.js';
import cors from 'cors';
import validateRequest, { detailValidatorRules, priceHistoryValidator, providerValidator } from './middleware/validators.js';
import PriceHistory from './models/price-history.js';
import multer from 'multer';
import MongoStore from 'connect-mongo';

mongoose.connect('mongodb://127.0.0.1:27017/autoparts').then(() => {
    console.log('Connected to MongoDB');
    updatePrices();
    setInterval(updatePrices, 5 * 60* 1000); 
}).catch(err => {
    console.error('Failed to connect to MongoDB', err);
});


function generateNextPrice(currentPrice) {
  const delta = currentPrice * (Math.random() * 0.2 - 0.1);
  return Math.max(1, Math.round(currentPrice + delta));
}

async function updatePrices() {
  try {
    const priceHistories = await PriceHistory.find({}).populate('detailId');

    for (const ph of priceHistories) {
      const lastPriceObj = ph.history[ph.history.length - 1];
      const currentPrice = lastPriceObj ? lastPriceObj.price : 100;

      const newPrice = generateNextPrice(currentPrice);

      const nextChange = new Date(Date.now() + 5 * 60 * 1000);
      ph.history.push({ price: newPrice, date: nextChange });
      await ph.save();
    }
  } catch (err) {
    console.log(err);
  }
}

const app = express();
const port = 7777;

app.use(express.json());

app.use(session({
  secret: "mysecret",
  resave: false,
  saveUninitialized: false,
  store: MongoStore.create({
    mongoUrl: 'mongodb://127.0.0.1:27017/autoparts',
    ttl: 2 * 60 * 60
  }),
  cookie: {
    httpOnly: true,
    sameSite: 'lax',
    maxAge: 2 * 60 * 60 * 1000
  }
}));

app.use(cors({
    origin: 'http://localhost:3000',
    credentials: true
}));

app.use(passport.initialize());
app.use(passport.session());

app.get('/auth/google', passport.authenticate('google', { scope: ['profile'], 
    prompt: 'select_account' }));

app.get('/', (req, res) => {
  res.send('Hasfsdfsdfello World!');
});

app.get('/auth/google/callback', 
  passport.authenticate('google', { failureRedirect: '/login' }),
  function(req, res) {
    res.redirect("http://localhost:3000/");
});

app.get('/profile', checkAuth, (req, res) => {
    res.json({ user: req.user });
});

app.get('/logout', (req, res) => {
    req.logout(err => {
        if (err) {
            return res.status(500).json({ message: 'Logout failed' });
        }
        res.redirect("http://localhost:3000/");
    });
  });

app.get('/details', DetailController.getAllDetails);
app.get('/details/:id', DetailController.getDetailById);
app.post('/details', checkAuth, detailValidatorRules, validateRequest, DetailController.createDetail);
app.patch('/details/:id', checkAuth, DetailController.updateDetail);
app.delete('/details/:id', checkAuth, DetailController.deleteDetail);
app.get('/details/:id/prices', DetailController.getDetailPriceHistory);
app.get('/details/:id/provider', DetailController.getDetailsByProvider);

app.get('/providers', ProviderController.getAllProviders);
app.get('/providers/:id', ProviderController.getProviderById);

app.post('/orders', checkAuth, OrderController.createOrder);
app.get('/orders', OrderController.getAllOrders);
app.get('/orders/:id', checkAuth, OrderController.getOrderById);

const storage = multer.memoryStorage();
const upload = multer({ storage });

app.post("/scan-image", checkAuth, upload.single("image"), DetectController.Detect);

app.listen(port, (err) => {
    if (err) {
        return console.log('Something bad happened', err);
    }
  console.log(`Server is running at http://localhost:${port}`);
});