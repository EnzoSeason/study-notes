# Interface

```c#
public interface ICalculator
{
  float Calculate();
}
```

Interface only has unimplemented methods.

```c#
public class Computer : ICalculator
{
  public float Calculate()
  {
    // TODO
  }
}
```

Interface serves as a **contract**. It tells what methods the class need to implement.

A class can extend multiple interfaces.
