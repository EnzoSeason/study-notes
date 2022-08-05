# Control flow

## Conditional statement

```c#
if (condtion)
{
  ...
}
else if (condition)
{
  ...
}
else
{
  ...
}
```

```c#
switch (role)
{
  case Role.Admin:
    ...
    break;
  case Role.User:
    ...
    break;
  default:
    ...
    break;
}
```

## Iteration statement

```c#
for (var i = 0; i < 10; i++)
{
  ...
}
```

```c#
foreach (var num in nums)
{
  ...
}
```

```c#
int i = 0;
while (i < 10)
{
  ...
  i++;
}
```

```c#
int i = 0;
do
{
  ...
  i++;
} while (i < 10);
```
