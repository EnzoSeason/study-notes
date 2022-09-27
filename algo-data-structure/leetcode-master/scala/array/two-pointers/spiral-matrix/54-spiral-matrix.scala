object Solution {
  def spiralOrder(matrix: Array[Array[Int]]): List[Int] = {
    val m = matrix.length
    val n = matrix(0).length
    val visited = scala.Array.ofDim[Boolean](m, n)
    val dx = Array(0, 1, 0, -1)
    val dy = Array(1, 0, -1, 0)
    var res = List[Int]()

    var direction = 0
    var i = 0
    var j = 0
    for (_ <- 0 until m * n) {
      res = res :+ matrix(i)(j)
      visited(i)(j) = true

      val nextI = (i + dx(direction)) % m
      val nextJ = (j + dy(direction)) % n
      if (nextI < 0 ||
        nextI >= m ||
        nextJ < 0 ||
        nextJ >= n ||
        visited(nextI)(nextJ)) {
        direction = (direction + 1) % 4
      }

      i += dx(direction)
      j += dy(direction)
    }
    res
  }
}