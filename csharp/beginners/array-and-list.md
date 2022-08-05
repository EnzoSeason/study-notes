# Array & List

## Array

Useful array's methods:

```c#
int[] nums = new int[3] { 9, 8, 7 };

// length
nums.Length;

// index
var i = Array.IndexOf(nums, 9)

// clear
// set the element to 0, false, or null.
Array.Clear(nums, 0, 2) // set first 2 elements to 0

// copy
int[] anotherNums = new int[2];
Array.Copy(nums, anotherNums, 2);

// sort
Array.Sort(nums);

// reverse
Array.Reverse(nums);
```

There are 2 different multi dimension arrays:

```c#
// Rectangular array
var matrix = new int[3, 5];
var element = matrix[0, 0];
```

```c#
// Jagged array
var matrix = new int[3][]; // matrix that has 3 rows.
martix[0] = new int[4]; // The first row has 4 columns.
```

## List

```c#
var nums = new List<int>();
var anotherNums = new List<int>() { 1, 2, 3 };
```

Userful methods:

```c#
var nums = new List<int>() { 1, 2, 3 };

// add
nums.Add(4);

// add range
nums.AddRange(new int[3] { 1, 5, 6});

// index of the first/last occured element
nums.IndexOf(1);
nums.LastIndexOf(1);

// length
nums.Count;

// remove an element
nums.Remove(9);

// remove all
nums.Clear();
```
