package playground

object Solution {
  def removeElement(nums: Array[Int], target: Int): Int = {
    if (nums.length == 0) return 0

    var slow = 0
    var fast = 0

    while (fast < nums.length) {
      if (nums(fast) != target) {
        nums(slow) = nums(fast)
        slow += 1
      }
      fast += 1
    }
    slow
  }
}