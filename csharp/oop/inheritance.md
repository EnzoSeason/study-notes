# Inheritance

## Constructor

- Base class constructors are called first.

- Base class constructors are not inherited.

```c#
public class Person
{
  private string _name;

  public Person(string name)
  {
    this._name = name;
  }
}

public class Customer : Person
{
  public Customer(string name)
    : base(name)
  {
    // TODO
  }
}
```

`base()` will call the constructors of the base class before initialization.

## Upcasting & Downcasting

- Upcasting: convert from a derived class to a base class.
- Downcasting: convert from a base class to a derived class.

### Upcasting

```c#
Person a = new Person("a");
Customer b = a; // safe, no extra action
```

### Downcasting

```c#
Person a = new Person("a");
Customer b = a;

Person c = (Person)b;
```

### as keyword

```c#
Customer c = person as Customer;
```

### is keyword

```c#
if (person is Customer)
{
  Customer c = person;
}
```
