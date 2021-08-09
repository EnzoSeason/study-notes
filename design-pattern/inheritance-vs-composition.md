# Inheritance vs Composition

Combination is better than inheritance, use **more combination less inheritance**.

The disadvantage of inheritance is when the tree of inheritance is **too deep** or **too wide**, it's hard to maintain and shared the codes among the classes.

For exemple, we want to create a class `Ostrich`. It can fly and lay eggs. If we use inheritance, we need to create 6 parents classes!

```code
Bird - | -   FlyBird  - | - FlyAndLayeggBird
       | _            _ | - FlyNotLayeggBird
       | - LayeggBrid - | - LayeggNotFlyBrid
```

If we use combination.

```java

public interface Flyable {
  void fly()；
}

public class FlyAbility implements Flyable {
  @Override
  public void fly() { //... }
}

//省略Tweetable/TweetAbility/EggLayable/EggLayAbility

public class Ostrich implements Tweetable, EggLayable { //鸵鸟
  private TweetAbility tweetAbility = new TweetAbility();  // combination
  private EggLayAbility eggLayAbility = new EggLayAbility(); // combination
  
  //... 省略其他属性和方法...
  
  @Override
  public void tweet() {
    tweetAbility.tweet(); // delegation
  }
  
  @Override
  public void layEgg() {
    eggLayAbility.layEgg(); // delegation
  }
}
```

To sum up:

- If the there are ONLY two layer in inheritance tree, the relation between the classes is **simple**. We can use inheritance.

- If the relation between the classes is **complicate**, we use combination.
