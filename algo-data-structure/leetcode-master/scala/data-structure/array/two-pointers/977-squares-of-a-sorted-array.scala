object Solution {
  def sortedSquares(nums: Array[Int]): Array[Int] = {
    var head = 0
    var tail = nums.length - 1
    val res = new Array[Int](nums.length)
    var i = tail

    while (i >= 0) {
      if (nums(head) * nums(head) > nums(tail) * nums(tail)) {
        res(i) = nums(head) * nums(head)
        head += 1
      } else {
        res(i) = nums(tail) * nums(tail)
        tail -= 1
      }
      i -= 1
    }

    res
  }
}