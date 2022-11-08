package org.jijie.spark.core.wordcount

import org.apache.spark.{SparkConf, SparkContext}

object WordCount extends App {

  // connect to Spark
  val conf = new SparkConf().setAppName("WordCount").setMaster("local")
  val sc = new SparkContext(conf)

  // run business logic
  val wordCount = sc
    .textFile("data")
    .flatMap(_.split(" "))
    .groupBy(word => word)
    .map {
      case (word, wordList) => (word, wordList.size)
    }
    .collect()

  wordCount.foreach(println)

  // close Spark
  sc.stop()
}
