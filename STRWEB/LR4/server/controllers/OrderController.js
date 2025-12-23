import Order from "../models/order.js";

export const createOrder = async (req, res) => {
  try {
    const userId = req.user._id;
    const { items } = req.body;

    if (!items || items.length === 0) {
      return res.status(400).json({ message: "Empty cart" });
    }

    const orderItems = items.map(item => ({
      detail: item._id,
      quantity: item.quantity,
      price: item.price
    }));

    const order = new Order({
      orderItems,
      user: userId
    });

    await order.save();

    res.status(201).json({ message: "Заказ успешно создан", order });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Server error" });
  }
};

export const getAllOrders = async (req, res) => {
    try {
        const orders = await Order.find().populate("orderItems.detail").populate("user");
        res.json(orders);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

export const getOrderById = async (req, res) => {
    try {
        const order = await Order.findById(req.params.id)
            .populate("orderItems.detail")
            .populate("user");

        if (!order) {
            return res.status(404).json({ message: "Order not found" });
        }

        res.json(order);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

