import { body, validationResult } from "express-validator";

export const detailValidatorRules = [
    body('name').isString().withMessage('Name must be a string').notEmpty().withMessage('Name is required'),
    body('article').isString().withMessage('Article must be a string').notEmpty().withMessage('Article is required'),
];

export const priceHistoryValidator = [
    body('price').isFloat({ gt: 0 }).withMessage('Price must be a number greater than 0').notEmpty().withMessage('Price is required').isFloat({ min: 0 })
        .withMessage('Price must be a number greater or equal to 0'),
];

export const providerValidator = [
    body('name').isString().withMessage('Name must be a string').notEmpty().withMessage('Name is required'),
    body('address').isString().withMessage('Address must be a string').notEmpty().withMessage('Address is required'),
    body('phone').matches(/^\+375(25|29|33|44)\d{7}$/).withMessage('Phone must be in format +375XXYYYYYYY')
];

export default function validateRequest(req, res, next) {
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
        return res.status(400).json({
            errors: errors.array()
        });
    }

    next();
}