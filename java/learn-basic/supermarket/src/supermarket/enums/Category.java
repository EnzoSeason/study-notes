package supermarket.enums;

public enum Category {
    FOOD(10, 300),
    COOK(200, 2000),
    SNACK(5, 100),
    CLOTHES(200, 1000),
    ELECTRIC(200, 10000);

    int lowestPrice;
    int highestPrice;

    Category(int lowestPrice, int highestPrice) {
        this.lowestPrice = lowestPrice;
        this.highestPrice = highestPrice;
    }

    public int getLowestPrice() {
        return lowestPrice;
    }

    public void setLowestPrice(int lowestPrice) {
        this.lowestPrice = lowestPrice;
    }

    public int getHighestPrice() {
        return highestPrice;
    }

    public void setHighestPrice(int highestPrice) {
        this.highestPrice = highestPrice;
    }
}
