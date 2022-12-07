// https://leetcode.com/problems/search-insert-position/

object Solution {
  def searchInsert(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (nums(mid) < target) left = mid + 1
      else if (nums(mid) > target) right = mid
      else return mid
    }
    left
  }
}
