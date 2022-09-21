// https://leetcode.com/problems/move-zeroes/


/*
* Brut:
* If the zero is met, insert it to the tail
*/
object SolutionBrut {
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

/*
* Follow up: fast slow pointers
* move non-zero element pointed by fast pointer to the front
*/
object SolutionFastSlowPointers {
  def moveZeroes(nums: Array[Int]): Unit = {
    var slow = 0
    var fast = 0

    while (fast < nums.length) {
      if (nums(fast) != 0) {
        nums(slow) = nums(fast)
        slow += 1
      }
      fast += 1
    }

    for (i <- slow until nums.length) {
      nums(i) = 0
    }
  }
}