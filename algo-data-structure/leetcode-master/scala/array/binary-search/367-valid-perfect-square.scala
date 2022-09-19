// https://leetcode.com/problems/valid-perfect-square/

object Solution {
  def isPerfectSquare(num: Int): Boolean = {
    if (num == 1) return true

    var left: BigInt = 1
    var right: BigInt = num
    while (left < right) {
      val mid = left + (right - left) / 2
      if (mid * mid < num) left = mid + 1
      else if (mid * mid > num) right = mid
      else return true
    }

    false
  }
}
