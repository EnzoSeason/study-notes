# Generic

```c#
public class MyList<T>
{
  public void Add(T value)
  {
    // TODO
  }

  public T this[int index]
  {
    get { throw new NotImplementedException(); }
  }
}

var nums = new MyList<int>();
var strs = new MyList<string>();
```

There are some userful interfaces for the generic. (e.g. `IComparable`)

```c#
public class Utils<T> where T : IComparable
{
  public T Max<T>(T a, T b)
  {
    return a.CompareTo(b) > 0 ? a : b;
  }
}

```

`T` can be:

- a value type (`where T : struct`)
- a reference type (`where T : class`)
- a class
- an interface
- has a constructor (`where T : new()`)
