import Detail from "../models/detail.js";
import PriceHistory from "../models/price-history.js";

export const getAllDetails = async (req, res) => {
    try {
        const details = await Detail.find().populate(['priceHistory', 'providers']);
        res.json(details);
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

export const getDetailById = async (req, res) => {
    try {
        const detail = await Detail.findById(req.params.id).populate(['priceHistory', 'providers']);
        if (!detail) {
            return res.status(404).json({ message: 'Detail not found' });
        }
        res.json(detail);
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

export const createDetail = async (req, res) => {
    try {
        const { name, article, price } = req.body;

        const newDetail = new Detail({
            name,
            article,
            priceHistory: null
        });

        const savedDetail = await newDetail.save();

        const history = new PriceHistory({
            detailId: savedDetail._id,
            history: [
                {
                    price: price,
                    date: new Date()
                }
            ]
        });

        const savedHistory = await history.save();

        savedDetail.priceHistory = savedHistory._id;
        await savedDetail.save();

        res.status(201).json(savedDetail);

    } catch (error) {
        console.error(error);
        if (error.code === 11000) {
            return res.status(400).json({
                message: "Not unique article",
                field: "article"
            });
        }
        res.status(500).json({ message: "Server Error" });
    }
};

export const updateDetail = async (req, res) => {
    try {
        const { name, article, price } = req.body;
        const detailId = req.params.id;

        const duplicate = await Detail.findOne({ article, _id: { $ne: detailId } });
        if (duplicate) {
            return res.status(400).json({ message: 'Артикул уже занят' });
        }

        const updatedDetail = await Detail.findById(detailId);
        if (!updatedDetail) {
            return res.status(404).json({ message: 'Detail not found' });
        }

        updatedDetail.name = name;
        updatedDetail.article = article;

        if (price != null && updatedDetail.priceHistory) {
            const priceHist = await PriceHistory.findById(updatedDetail.priceHistory);
            if (priceHist) {
                const history = priceHist.history;
                const index = history.length > 1 ? history.length - 2 : history.length - 1;
                history[index].price = price;
                await priceHist.save();
            }
        }

        await updatedDetail.save();

        res.json(updatedDetail);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Server Error' });
    }
};


export const deleteDetail = async (req, res) => {
    try {
        const deletedDetail = await Detail.findByIdAndDelete(req.params.id);    
        if (!deletedDetail) {
            return res.status(404).json({ message: 'Detail not found' });
        }
        res.json({ message: 'Detail deleted successfully' });
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

export const getDetailPriceHistory = async (req, res) => {
    try {
        const { id } = req.params;

        const detail = await Detail.findById(id).populate('priceHistory');
        if (!detail || !detail.priceHistory) {
          return res.status(404).json({ error: 'Price history not found' });
        }

        const history = detail.priceHistory.history
            .sort((a, b) => new Date(b.date) - new Date(a.date)) 
            .slice(0, 10) 
            .reverse(); 

        res.json(history);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
};

export const getDetailsByProvider = async (req, res) => {
  try {
    const { id } = req.params; 

    const filter = {};

    if (id) {
      filter.providers = id; 
    }

    const details = await Detail.find(filter)
      .populate("priceHistory")
      .populate("providers");

    res.json(details);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Server Error" });
  }
};

