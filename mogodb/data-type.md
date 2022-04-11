## Data Types

The full doc is here: [BSON Types](https://docs.mongodb.com/manual/reference/bson-types/)

> The language used in `mongosh` is **javascript**.

### ObjectId

It's the **ID** of the document in the collection.

### String

The limit is the **16mb**.

### Boolean

### Number

By default, it's `double`. It's _float64_. However, there are other types.

- Integer: It's _int32_ (+- 2<sup>32</sup>). It's created by `new NumberInt()` in `mongosh`.

- NumberLong: It's _int64_ (+- 2<sup>64</sup>). It's created by `new NumberLong()` in `mongosh`.

- NumberDecimal: It's very precise. It's created by `new NumberDecimal()` in `mongosh`.

### Date

There are:

- ISODate: It can be created by `new Date()` in `mongosh`.

- Timestamp: It can be created by `new Timestamp()` in `mongosh`.

### Array

### Embedded document

The limit is the **16mb**.


Additionally, you may only have **100 levels** of embedded documents.