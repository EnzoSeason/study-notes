package org.jijie.spark.core.wordcount

import org.apache.spark.{SparkConf, SparkContext}

object WordCount2 extends App {

  // connect to Spark
  val conf = new SparkConf().setAppName("WordCount").setMaster("local")
  val sc = new SparkContext(conf)

  // run business logic
  val wordCount = sc
    .textFile("data")
    .flatMap(_.split(" "))
    .map((_, 1))
    .groupBy(_._1)
    .map {
      case (_, wordTuples) =>
        wordTuples.reduce((t1, t2) => (t1._1, t1._2 + t2._2))
    }
    .collect()

  wordCount.foreach(println)

  // close Spark
  sc.stop()
}
