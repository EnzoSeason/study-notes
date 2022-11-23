package supermarket.interfaces;

import supermarket.enums.Category;

public interface Merchandise {
    /**
     * Get the name of the merchandise
     * @return name of the merchandise
     */
    String getName();

    /**
     * Get the price during the discount
     * @return a price
     */
    double getDiscountPrice();

    /**
     * Get the original price
     * @return a price
     */
    double getOriginalPrice();

    /**
     * Get the category of the merchandise
     * @return a category
     */
    Category getCategory();

    /**
     * Get the number of the merchandise
     * @return an amount
     */
    int getAmount();

    /**
     * Buy the merchandises
     * @param amount the amount of the merchandise bought
     */
    void buy(int amount);

    /**
     * Put back the merchandises
     * @param amount the amount of the merchandise put back
     */
    void putBack(int amount);

}
