# Expression

## Instruction vs Expression

Instruction tells the computer **to do** something, such as changing a variable, printing in the console, etc.

Expression is something that **has a value or a type**.

For exemple:

```scala
var aCondition = true;
val aConditionValue = if(aCondition) 5 else 3
```

It's a `IF Expression`. It **always returns a value**.

> `IF Expression` is very useful in Scala.

**Everything in Scala is an Expression**.

## Code block

The code block is an expression. The value of a code block is that of the its last expression.

```scala
val aCodeBlock = {
  val z = 3
  if (z > 2) "hello" else "bye"
}
```

The value or variable declared inside the code block can't be accessed by the outside.


