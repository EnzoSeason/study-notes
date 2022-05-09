# Infinite Sequence

With `LazyList`, we can define an infinite sequence.

```scala
def from(start: Int): LazyList[Int] = start #:: from(start + 1)

val nats = from(0) // not computed
val nats10 = nats.take(10) // not computed
val nats10List = nats10.toList // computed
```

## Example: The Sieve of Eratosthenes

It's a way to get prime numbers.

The idea is

- start with `2`, the first prime number, and remove all the multiples of 2.

- Then go to `3`, the next prime number, and do the same thing

- Then `5`, ...

```scala
def sieve(s: LazyList[Int]): LazyList[Int] =
  s.head #:: sieve(s.tail.filter(_ % s.head != 0))

val primes = sieve(from(2))

println(primes.take(10).toList)
// List(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
```

## Example: guess the square root

```scala 
def sqrtSeq(x: Double): LazyList[Double] = {
  def improve(guess: Double) = (guess + x / guess) / 2
  lazy val guesses: LazyList[Double]  = 1 #:: guesses.map(improve)
  guesses
}
```

The lazy list of guesses is as followed.

```code
1 #:: i(1) #:: i(i(1)) #:: i(i(i(1))) ...
```
> `i` is the shortname of `improve`.


```scala
def isGoodEnough(guess: Double, x: Double): Boolean = {
  math.abs((guess * guess) - x) < 0.001
}

val guesses = sqrtSeq(2).filter(isGoodEnough(_, 2))
println(guesses.head)
```
