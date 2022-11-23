package supermarket.interfaces;

import supermarket.ShoppingCart;
import supermarket.enums.Category;

public interface Customer {
    String getCustomerId();

    /**
     * The preparation for shopping
     */
    void startShopping();

    /**
     * @return a Category whose merchandises are wanted by the customer
     */
    Category pickCategory();

    /**
     * The customer decides to buy a merchandise.
     *
     * @param merchandise that customer want to buy
     * @return the number of the merchandise bought.
     */
    int buy(Merchandise merchandise);

    /**
     * Whether to check out or not
     * @return true: check out, false: keep shopping
     */
    boolean isCheckOut();

    /**
     * Pay for the shopping
     *
     * @param shoppingCart it contains the merchandises that the customer want to buy
     * @param actualCost The cost after the supermarket discount
     * @return the spent money if payment is successful. Otherwise, -1
     */
    double pay(ShoppingCart shoppingCart, double actualCost);

    /**
     *
     * @return the money spent on shopping
     */
    double getTotalSpentMoney();
}
