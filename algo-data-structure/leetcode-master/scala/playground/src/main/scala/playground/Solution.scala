package playground

object Solution {
  def searchRange(nums: Array[Int], target: Int): Array[Int] = {
    val result = Array(-1, -1)
    var left = 0
    var right = nums.length

    // search the left boundary
    while (left < right) {
      val mid = left + (right - left) / 2
      if (nums(mid) < target) left = mid + 1
      else right = mid
    }

    if (left == nums.length || nums(left) != target)
      return Array(-1, -1)
    result(0) = right

    // search the right boundary
    left = 0
    right = nums.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (nums(mid) > target) right = mid
      else left = mid + 1
    }

    result(1) = left - 1
    result
  }
}