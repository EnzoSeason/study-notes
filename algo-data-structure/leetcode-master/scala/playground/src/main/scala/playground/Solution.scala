package playground

object Solution {
  def threeSum(nums: Array[Int]): List[List[Int]] = {
    scala.util.Sorting.quickSort(nums)
    var result = List[List[Int]]()

    var i = 0
    while (i < nums.length) {
      if (nums(i) > 0) return result

      while (i > 0 && i < nums.length && nums(i) == nums(i - 1)) {
        i += 1
      }

      var left = i + 1
      var right = nums.length - 1
      while (left < right) {
        val localSum = nums(i) + nums(left) + nums(right)
        if ( localSum == 0) {
          result = (nums(i) :: nums(left) :: nums(right) :: Nil) :: result
          left += 1
          while (left < nums.length && nums(left) == nums(left - 1)){
            left += 1
          }
          right -= 1
          while (right > 0 && nums(right) == nums(right + 1)) {
            right -= 1
          }
        }
        else if (localSum < 0) {
          left += 1
        }
        else {
          right -= 1
        }
      }

      i += 1
    }
    result
  }
}