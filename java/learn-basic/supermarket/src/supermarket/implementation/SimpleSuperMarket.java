package supermarket.implementation;

import supermarket.enums.Category;
import supermarket.interfaces.Merchandise;
import supermarket.interfaces.Supermarket;

import java.util.Map;

public class SimpleSuperMarket implements Supermarket {
    private final String name = "Simple Supermarket";
    private final int sampleCount = 5;

    private Merchandise[] items;
    private int[] itemsAmounts;
    private long totalIncome;

    public SimpleSuperMarket(Merchandise[] items) {
        this.items = items;
        itemsAmounts = new int[items.length];
        for (int i = 0; i < items.length; i++) {
            itemsAmounts[i] = items[i].getAmount();
        }
    }

    @Override
    public Merchandise[] getAll() {
        return items;
    }

    @Override
    public Merchandise[] getSome(Category category) {
        Merchandise[] results = new Merchandise[sampleCount];
        int idx = 0;
        for (Merchandise m : items) {
            if (idx >= sampleCount)
                break;
            if (m.getCategory() == category && Math.random() > 0.5) {
                results[idx] = m;
                idx += 1;
            }
        }
        return results;
    }

    @Override
    public void addIncome(double income) {
        this.totalIncome += income;
    }

    @Override
    public void dailyReport() {
        System.out.println(this.name + " earns " + this.totalIncome);
        System.out.println("Selling numbers are as followed.");
        for (int i = 0; i < items.length; i++) {
            System.out.println(
                    items[i].getCategory().name() + "\t" +
                            items[i].getName() + "\t" +
                            (items[i].getAmount() - itemsAmounts[i]));
        }
    }

    public String getName() {
        return name;
    }
}
