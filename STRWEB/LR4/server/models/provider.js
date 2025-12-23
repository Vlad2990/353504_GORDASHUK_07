import mongoose from 'mongoose';

const ProviderSchema = new mongoose.Schema({
    name: { type: String, required: true, unique: true },
    address: { type: String, required: true },
    phone: { type: String, required: true }
    }, {
    timestamps: true
});

export default mongoose.model('Provider', ProviderSchema);