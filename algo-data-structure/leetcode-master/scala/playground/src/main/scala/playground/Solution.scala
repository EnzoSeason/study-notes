package playground

object Solution {
  def moveZeroes(nums: Array[Int]): Unit = {
    var head = 0
    var tail = nums.length

    while (head < tail) {
      if (nums(head) == 0) {
        for (i <- head until tail - 1) {
          nums(i) = nums(i + 1)
        }
        nums(tail - 1) = 0
        tail -= 1
      } else {
        head += 1
      }
    }
  }
}