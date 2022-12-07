object Solution {
  def fourSum(nums: Array[Int], target: Int): List[List[Int]] = {
    scala.util.Sorting.quickSort(nums)
    var res = List[List[Int]]()

    var i = 0
    while (i < nums.length) {
      while (i > 0 && i < nums.length - 3 && nums(i) == nums(i - 1)) i += 1

      var j = i + 1
      while (j < nums.length) {
        while (j > i + 1 && j < nums.length - 2 && nums(j) == nums(j - 1)) j += 1
        var left = j + 1
        var right = nums.length - 1
        while (left < right) {
          val localSum = BigInt(nums(i)) + BigInt(nums(j)) + BigInt(nums(left)) + BigInt(nums(right))
          if (localSum < -BigInt(Int.MaxValue) || localSum.toInt < target) {
            left += 1
          } else if (localSum > BigInt(Int.MaxValue) || localSum.toInt > target) {
            right -= 1
          } else {
            res = (nums(i) :: nums(j) :: nums(left) :: nums(right) :: Nil) :: res
            left += 1
            while (left < right && nums(left) == nums(left - 1)) left += 1
            right -= 1
            while (left < right && nums(right) == nums(right + 1)) right -= 1
          }
        }
        j += 1
      }
      i += 1
    }
    res
  }
}