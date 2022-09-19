package playground

object Solution {
  def mySqrt(x: Int): Int = {
    var left: BigInt = 1
    var right: BigInt = x

    while (left < right) {
      val mid = left + (right - left) / 2
      if (mid * mid < x)
        if ((mid + 1) * (mid + 1) > x) return mid.toInt
        else left = mid + 1
      else if (mid * mid > x) right = mid
      else return mid.toInt
    }
    x
  }
}