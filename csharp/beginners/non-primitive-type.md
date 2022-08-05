# Non primitive type

## Class

```c#
public class Person
{
  public string Name;

  public void Greet()
  {
    Console.WriteLine("Hi, my name is " + Name);
  }
}
```

## Struct

Struct is similar to class. But, it's smaller and less powerful. It's useful for creating a commonly reused simple object. For example, a point has x and y.

```c#
public struct Point
{
  public int X;
  public int Y;
}
```

## Array

In c#, array has a **fixed size**.

```c#
// init an array with ten 0
int[] nums = new int[10];

// init an array with the content.
int[] counts = new int[3] {1, 2, 3};

// get an element of an array by index
Console.WriteLine(nums[0]);
```

## String

String is **immutable**. If you want to build a complex string, use `StringBuilder` class.

To join the string:

```c#
// option 1
const string name = firstName + " " + lastName;

// option 2
const string name = string.Format("{0} {1}", firstName, lastName);

// option 3
const string[] words = new string[2] {firstName, lastName};
const string name = string.Join(" ", words);
```

## Enum

```c#
public enum PayMethod
{
  Cash = 0,
  Card = 1,
  Phone = 2
}

var method = PayMethod.Card
```

By default, the elements of `enum` is `int`. We can set it to `byte`.

```c#
public enum PayMethod : byte
```

```c#
// int to enum
const int methodId = 1;
var method = (PayMethod)methodId;

// enum to string
string methodName = method.ToString();

// string to enum
var method = (PayMethod)Enum.Parse(typeof(PayMethod), "Card");
```

## Value type vs Reference type

Value type includes `primitive` and `struct`. It is allocated on the **stack**. Memory allocation is done **automatically**. It will be **removed immediately** when it's out of memory.

Reference type inclues `non primitive`. It is allocated on the **heap**. Memory allocation is done by manually `new`. The memory is released by **garbage collection** of **CLR**.
