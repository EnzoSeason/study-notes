package designPattern;

public class SingletonEdge {
    private SingletonEdge() {
    }

    private static SingletonEdge se = new SingletonEdge();

    public static SingletonEdge getInstance() {
        return se;
    }
}
