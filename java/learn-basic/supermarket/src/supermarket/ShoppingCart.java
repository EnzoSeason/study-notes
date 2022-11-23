package supermarket;

import supermarket.interfaces.Merchandise;

import java.util.Date;

public class ShoppingCart {
    private Merchandise[] items;
    private int[] itemAmounts;
    private int currIndex;
    private int maxAmount;

    public ShoppingCart(int maxAmount) {
        this.items = new Merchandise[maxAmount];
        this.itemAmounts = new int[maxAmount];
        this.currIndex = 0;
        this.maxAmount = maxAmount;
    }

    public boolean canAddMore() {
        return this.currIndex < this.maxAmount;
    }

    public boolean add(Merchandise merchandise, int amount) {
        if (!this.canAddMore())
            return false;
        this.items[this.currIndex] = merchandise;
        this.itemAmounts[this.currIndex] = amount;
        this.currIndex += 1;
        merchandise.buy(amount);
        return true;
    }

    public double getOriginalCost(){
        double cost = 0;
        int idx = 0;
        for (Merchandise merchandise: this.items) {
            if (merchandise == null)
                continue;
            cost += merchandise.getOriginalPrice() * this.itemAmounts[idx];
            idx += 1;
        }
        return cost;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("===========================\n");
        sb.append("Shopping at: ").append(new Date()).append("\n");

        int idx = 0;
        for (Merchandise merchandise: this.items) {
            if (merchandise == null)
                continue;
            sb
                    .append(merchandise.getCategory().name()).append("\t")
                    .append(merchandise.getName()).append("\t")
                    .append(this.itemAmounts[this.currIndex]).append("\t")
                    .append(merchandise.getOriginalPrice() * this.itemAmounts[this.currIndex]).append("\t");
            idx += 1;
        }
        sb.append("Total Original Cost: ").append(this.getOriginalCost()).append("\n");
        sb.append("===========================\n");
        return sb.toString();
    }
}
