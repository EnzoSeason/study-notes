# Exception

```c#
try
{
  var streamRead = new SteamReader("");
}
catch (DividedByZeroException ex) // The most specific exception
{
  // TODO
}
catch (Exception ex) // The most generic exception
{
  // TODO
}
finally
{
  streamReader.Dispose();
}
```

In C#, some classes are not managed by CLR. We need to dispose them manually in `finally`.

These classes are usually related to files, database connection, network connection, etc.

## using keyword

`using` in the C# will create a `finally` block under the hood, which will call the `dispose()` automatically

```c#
try
{
  using (var streamRead = new SteamReader(""))
  {
    var content = streamRead.ReadToEnd();
  }
}
catch (Exception ex)
{
  // TODO
}
```

## Custom Exception

```c#
public class CustomException : Exception
{
  public CustomException(string message, Exception innerException)
    : base(message, innerException)
  {}
}
```