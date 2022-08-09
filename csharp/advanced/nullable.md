# Nullable

```c#
string? name;
```

It means `name` is `string` or ``null`.

To read it safely:

```c#
name.GetValueOrDefault();
```

C# supports conditional operator.

```c#
string john = (name != null) ? name : "John";
```

C# supports null coalescing operator.

```c#
string john = name ?? "Jonh";
```
