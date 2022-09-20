// https://leetcode.com/problems/remove-element/

// Brut
// If the target is met, bubble up it to the tail

object SolutionBrut {
  def removeElement(nums: Array[Int], target: Int): Int = {
      var head = 0
      var tail = nums.length
      
      while (head < tail) {
          if (nums(head) == target) {
              for (i <- head until tail - 1) {
                  nums(i) = nums(i + 1)
              }
              tail -= 1
          } else {
            head += 1
          }
      }
      tail
  }
}

// follow-up
// replace inner loop by swapping head element with the tail

object SolutionSwap {
  def removeElement(nums: Array[Int], target: Int): Int = {
      var head = 0
      var tail = nums.length
      
      while (head < tail) {
          if (nums(head) == target) {
              nums(head) = nums(tail - 1)
              nums(tail - 1) = target
              tail -= 1
          } else {
              head += 1
          }
      }
      tail
  }
}

// follow up 2
// Use fast pointer to traverse all the non-targeted element
// and move them to the front

object SolutionFastSlowPointers {
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