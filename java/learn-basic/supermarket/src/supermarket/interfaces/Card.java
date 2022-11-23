package supermarket.interfaces;

import supermarket.ShoppingCart;

/**
 * The card is owned by the customer. Its owner can have extra discount
 */
public interface Card {
    /**
     *
     * @param customer the card owner
     * @param shoppingCart the shopping cart of the card owner
     * @param originalCost the original cost of all the merchandise in the shopping cart
     * @param actualCost the actual cost of all the merchandise in the shopping cart before applying the card
     * @return the money the card owner benefited by applying the card
     */
    double applyCardDiscount(Customer customer, ShoppingCart shoppingCart, double originalCost, double actualCost);
}
