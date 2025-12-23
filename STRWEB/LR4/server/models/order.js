import mongoose from "mongoose";

const OrderSchema = new mongoose.Schema({
  orderItems: [
    {
      detail: { type: mongoose.Schema.Types.ObjectId, ref: "Detail", required: true },
      quantity: { type: Number, required: true },
      price: { type: Number, required: true }
    }
  ],
  orderDate: { type: Date, default: Date.now },
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }
  }, {
  timestamps: true
});

export default mongoose.model("Order", OrderSchema);