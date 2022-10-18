package playground

import scala.annotation.tailrec

object Solution {
  def fourSumCount(nums1: Array[Int], nums2: Array[Int], nums3: Array[Int], nums4: Array[Int]): Int = {
    val n = nums1.length
    var cache = Map[Int, Int]()
    var count = 0

    for {
      i <- 0 until n
      j <- 0 until n
    } {
      val localSum = nums1(i) + nums2(j)
      cache.get(localSum) match {
        case Some(value) => cache += (localSum -> (value + 1))
        case None => cache += (localSum -> 1)
      }
    }

    for {
      k <- 0 until n
      l <- 0 until n
    } {
      val localSum = - (nums3(k) + nums4(l))
      cache.get(-localSum) match {
        case Some(value) => count += value
        case None => null
      }
    }

    count
  }
}