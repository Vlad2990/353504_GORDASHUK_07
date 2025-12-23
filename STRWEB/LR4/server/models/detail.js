import mongoose from 'mongoose';

const DetailSchema = new mongoose.Schema({
    name: { type: String, required: true },
    article: { type: String, required: true, unique: true },
    providers: [
        { type: mongoose.Schema.Types.ObjectId, ref: "Provider" }
    ],

    priceHistory: { type: mongoose.Schema.Types.ObjectId, ref: "PriceHistory" }
    }, {
    timestamps: true
});

export default mongoose.model('Detail', DetailSchema);