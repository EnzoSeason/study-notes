# Date

## DateTime

`DateTime` object is immutable.

```c#
var dateTime = new DateTime(2022, 8, 5);
var now = DateTime.Now;
var today = DateTime.Today;

var tomorrow = now.AddDays(1);
var yesterday = now.AddDays(-1);

now.ToString("yyyy-MM-dd HH:mm");
```

## TimeSpan

```c#
// 2h 1 min
var timeSpan = new TimeSpan(2, 1, 0);

timeSpan.Minutes;
timeSpan.TotalMinutes;

// add 2 min
timeSpan.Add(TimeSpan.FromMinutes(2))

// to string
timsSpan.ToString();

// Parse string to TimeSpan
TimeSpan.Parse("02:01:00");
```
