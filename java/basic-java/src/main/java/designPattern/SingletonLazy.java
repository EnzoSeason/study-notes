package designPattern;

public class SingletonLazy {
    private SingletonLazy() {
    }

    private static SingletonLazy sl = null;

    public static SingletonLazy getInstance() {
        if (sl == null) {
            sl = new SingletonLazy();
        }
        return sl;
    }
}
