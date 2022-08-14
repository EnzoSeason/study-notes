# LINQ

LINQ is Language Integrated Query. It can query:

- Objects in memory (e.g. collection)
- Database
- XML
- ADO.NET data sets

```c#
using Sysytem.Linq;

// LINQ Query opertions
var cheapBooks =
  from b in books
  where b.Price < 10
  orderby b.Title

// LINQ extension Method
var cheapBooks = books
                    .Where(b => b.Price < 10)
                    .OrderBy(b => b.Title);
```

There are some useful extensions:

- Where
- Single
- SingleOrDefault
- First
- FirstOrDefault
- Min
- Max
- Average
- Skip
- Take
- ...
