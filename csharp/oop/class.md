# Class

## Constructor

```c#
public class Person
{
  public Person()
  {
    ...
  }
}
```

```c#
public class Person
{
  public string Name;

  public Person(string name)
  {
    this.Name = name;
  }
}
```

These 2 constructors can be overloaded.

```c#
public class Person
{
  public string Name;

  public Person()
  {
    ...
  }

  public Person(string name)
  {
    this.Name = name;
  }
}
```

A constructor can be called after another is called. It's very useful when we use the constructor overloading.

```c#
public class Person
{
  public string Name;
  public List<int> Scores;

  public Person()
  {
    Scores = new List<int>();
  }
  // This constructor call will invoke previous one's call.
  public Person(string name)
    : this()
  {
    this.Name = name;
  }
}
```

### Object initializer

It's a way to initialize an object only call the parametreless constructor and pass the parametres.

```c#
var joe = new Person { Name = "Joe" };
```

## Methods

Methods can be overloaded, too.

To pass the parametres easier, c# has **params modifier**. By using the `params` keyword, you can specify a method parameter that takes a variable number of arguments. The parameter type must be a **single-dimensional array**.

```c#
public class Calculator
{
  public int Add(params int[] nums){}
}

var a = calculator.Add(new int[] { 1, 2, 3 });
var a = calculator.Add(1, 2, 3);
```

### Getter & Setter

Simple version:

```c#
public class Person
{
  private string _name;

  public string Name
  {
    get { return _name; }
    set { _name = value; }
  }
}
```

Even simpler:

```c#
public class Person
{
  public string Name { get; set; }
}
```

### Indexer

```c#
var cookie = new HttpCookie();

// to make this line happen, we need to create an indexer.
var headers = cookie["headers"];
```

```c#
public class HttpCookie
{
  private readonly Dictionary<string, string> _dict = new ictionary<string, string>();

  // indexer
  public string this[string key]
  {
    get { return _dict[key]; }
    set { _dict[key] = value; }
  }
}
```
