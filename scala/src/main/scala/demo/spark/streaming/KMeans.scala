package demo.spark.streaming

import java.util.Calendar

import org.apache.spark.SparkConf
import org.apache.spark.mllib.clustering.StreamingKMeans
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.streaming.{Seconds, StreamingContext}


/**
 * Demo of streaming k-means with Spark Streaming.
 * Reads data from one directory, and prints models and predictions to another.
 *
 * Run via top-level executable:
 *
 * spark-streaming-demo kmeans opts
 *
 */

object KMeans {

  def main(args: Array[String]) {
    if (args.length != 7) {
      System.err.println(
        "Usage: KMeans " +
          "<inputDir> <outputDir> <batchDuration> <numClusters> <numDimensions> <halfLife> <batchUnit>")
      System.exit(1)
    }

    val (inputDir, outputDir, batchDuration, numClusters, numDimensions, halfLife, timeUnit) =
      (args(0), args(1), args(2).toLong, args(3).toInt, args(4).toInt, args(5).toFloat, args(6))

    val conf = new SparkConf().setMaster("local").setAppName("KMeansDemo")
    val ssc = new StreamingContext(conf, Seconds(batchDuration))

    val trainingData = ssc.textFileStream(inputDir).map(Vectors.parse)

    val model = new StreamingKMeans()
      .setK(numClusters)
      .setHalfLife(halfLife, timeUnit)
      .setRandomCenters(numDimensions, 0.0)

    model.trainOn(trainingData)

    val predictions = model.predictOn(trainingData)

    predictions.foreachRDD { rdd =>
      val modelString = model.latestModel().clusterCenters
        .map(c => c.toString.slice(1, c.toString.length-1)).mkString("\n")
      val predictString = rdd.map(p => p.toString).collect().mkString("\n")
      val dateString = Calendar.getInstance().getTime.toString.replace(" ", "-").replace(":", "-")
      Utils.printToFile(outputDir, dateString + "-model", modelString)
      Utils.printToFile(outputDir, dateString + "-predictions", predictString)
    }

    ssc.start()
    ssc.awaitTermination()
  }
}
