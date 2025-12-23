import Provider from '../models/Provider.js';

export const getAllProviders = async (req, res) => {
    try {
        const providers = await Provider.find();
        res.json(providers);
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Server Error' });
    }
};

export const getProviderById = async (req, res) => {
    try {
        const provider = await Provider.findById(req.params.id);
        if (!provider) {
            return res.status(404).json({ message: 'Provider not found' });
        }
        res.json(provider);
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: 'Server Error' });
    }
};
