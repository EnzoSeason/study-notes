package playground

object Solution {
  def totalFruit(fruits: Array[Int]): Int = {
    val bag = collection.mutable.Map[Int, Int]()
    var res = 0

    var left = 0
    var right = 0
    while (right < fruits.length) {
      bag(fruits(right)) = bag.getOrElse(fruits(right), 0) + 1

      while (bag.size > 2) {
        bag(fruits(left)) -= 1

        if (bag(fruits(left)) == 0) bag -= fruits(left)

        left += 1
      }

      res = math.max(right - left + 1, res)
      right += 1
    }

    res
  }
}