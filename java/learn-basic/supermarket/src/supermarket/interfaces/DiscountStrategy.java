package supermarket.interfaces;

import supermarket.ShoppingCart;

/**
 * The discount strategy is applied on the entire supermarket.
 */
public interface DiscountStrategy {
    double discount(ShoppingCart shoppingCart);
}
