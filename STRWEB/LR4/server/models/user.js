import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
    googleId: { type: String, required: true, unique: true },
    displayName: { type: String, required: true }
});

export const User = mongoose.model('User', userSchema);