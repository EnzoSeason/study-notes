// https://leetcode.com/problems/binary-search/

object Solution {
  def search(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (nums(mid) > target) right = mid
      else if (nums(mid) < target) left = mid + 1
      else return mid
    }
    -1
  }
}
