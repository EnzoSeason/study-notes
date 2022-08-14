# Extension

Extension add extra methods to an existing class.

There are some rules:

1. Extension is a static class
2. The method is static
3. The first parameter of the method is `this T target`.

```c#
namespace MyExtension
{
  public static class StringExtensions
  {
    public static string Shorten(this String str, int numOfWords)
    {
      if (numOfWords == 0)
        return "";

      var words = str.Split(" ");
      if (words.Length <= numOfWords)
        return str

      return string.Join(" ", words.Take(numOfWords));
    }
  }
}
```

```c#
using MyExtension.StringExtensions;

var post = ".......";
var shortPost = post.Shorten(3);
```

Extension is rarly created by the developers. Devlopers usually use them. (e.g. `Linq`)
