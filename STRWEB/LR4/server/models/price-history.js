import mongoose from "mongoose";

const priceHistorySchema = new mongoose.Schema({
    detailId: { type: mongoose.Schema.Types.ObjectId, ref: 'Detail', required: true },

    history: [
        {
            price: { type: Number, required: true },
            date: { type: Date, default: Date.now }
        }
    ]
    }, {
    timestamps: true
});

export default mongoose.model('PriceHistory', priceHistorySchema);