object Solution {
  def generateMatrix(n: Int): Array[Array[Int]] = {
    var left = 0
    var right = n - 1
    var top = 0
    var bottom = n - 1
    var num = 1
    val res = scala.Array.ofDim[Int](n, n)

    while (left <= right && top <= bottom) {
      if (left == right && top == bottom) {
        res(top)(left) = num
        return res
      }

      for (j <- left until right) {
        res(top)(j) = num
        num += 1
      }

      for (i <- top until bottom) {
        res(i)(right) = num
        num += 1
      }

      for (j <- right until left by -1) {
        res(bottom)(j) = num
        num += 1
      }

      for (i <- bottom until top by -1) {
        res(i)(left) = num
        num += 1
      }
      left += 1
      top += 1
      right -= 1
      bottom -= 1
    }
    res
  }
}