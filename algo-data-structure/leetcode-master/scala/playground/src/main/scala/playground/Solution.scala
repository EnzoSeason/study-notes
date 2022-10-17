package playground

import scala.annotation.tailrec

object Solution {
  def isHappy(n: Int): Boolean = {
    def getNextNumFromString(n: BigInt): BigInt = {
      var localSum: BigInt = 0
      for (c <- n.toString) {
        val num = c.asDigit
        localSum += num * num
      }
      localSum
    }

    @tailrec
    def getNextNumFromNumber(n: BigInt, acc: BigInt): BigInt = {
      if (n == 0) acc
      else {
        val localSum = (n % 10) * (n % 10)
        getNextNumFromNumber(n / 10, acc + localSum)
      }
    }

    @tailrec
    def isHappyRec(n: BigInt, history: Set[BigInt]): Boolean = {
      if (n == 1) return true
      if (history contains n) false
      else isHappyRec(getNextNumFromNumber(n, 0), history + n)
    }

    isHappyRec(n, Set[BigInt]())
  }
}