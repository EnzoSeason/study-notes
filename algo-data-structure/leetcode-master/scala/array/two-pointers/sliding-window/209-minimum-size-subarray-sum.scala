object Solution {
  def minSubArrayLen(target: Int, nums: Array[Int]): Int = {
    var left = 0 // the left boundary of sliding window
    var localSum = 0
    var res = Int.MaxValue

    // The right boundary of sliding window is included
    for (right <- 0 until nums.length) {
      localSum += nums(right)
      while (localSum >= target) {
        res = math.min(right - left + 1, res)
        localSum -= nums(left)
        left += 1
      }
    }

    if (res == Int.MaxValue) 0 else res
  }
}