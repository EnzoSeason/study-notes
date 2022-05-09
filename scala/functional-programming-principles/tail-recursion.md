# Tail recursion

If a function **calls itself as its last action**, the function's stack frame can be reused. This is tail recursion.


```scala
import scala.annotation.tailrec

@tailrec
def gcd(a: Int, b: Int): Int = 
  if (b == 0) a else gcd(b, a % b)
```