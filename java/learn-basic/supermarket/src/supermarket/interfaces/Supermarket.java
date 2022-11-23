package supermarket.interfaces;

import supermarket.enums.Category;

public interface Supermarket {
    /**
     * Get all the merchandises
     * @return An array of merchandises
     */
    Merchandise[] getAll();

    /**
     * Get some merchandises randomly of the given category
     * @param category a category of the merchandise
     * @return An array of merchandises
     */
    Merchandise[] getSome(Category category);

    /**
     * Add the income to total earned money
     * @param income  earned money by selling merchandises
     */
    void addIncome(double income);

    /**
     * Generate the daily business report
     */
    void dailyReport();
}
