# Polymorphism

## Method overriding

```c#
public class Animal
{
  public virtual void Walk()
  {
    // default implementation
  }
}

public class Person : Animal
{
  public override void Walk() {}
}
```

`virtual` in the base class indicates the method can be overrided.

`override` means the method is overrided.

## Abstract class

```c#
public abstract class Animal
{
  public abstract void Walk();
}

public class Person : Animal
{
  public override void Walk() {}
}
```

## Sealed

`sealed` prevents **derivation** of a class and **overriding** of a method.
