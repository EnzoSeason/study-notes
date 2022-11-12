package org.jijie.spark.core.wordcount

import org.apache.spark.{SparkConf, SparkContext}

object WordCount3 extends App {

  // connect to Spark
  val conf = new SparkConf().setAppName("WordCount").setMaster("local")
  val sc = new SparkContext(conf)

  // run business logic
  val wordCount = sc
    .textFile("data")
    .flatMap(_.split(" "))
    .map((_, 1))
    // Spark function: reduce the values of the same key
    .reduceByKey(_ + _)
    .collect()

  wordCount.foreach(println)

  // close Spark
  sc.stop()
}
