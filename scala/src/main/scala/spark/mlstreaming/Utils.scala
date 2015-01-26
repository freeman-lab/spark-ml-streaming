package spark.mlstreaming

import java.io.{FileWriter, BufferedWriter, File}

/**
 * Utilities for streaming demos
 */

object Utils {

  def printToFile(pathName: String, fileName: String, contents: String) = {
    val file = new File(pathName + "/" + fileName + ".txt")
    val bw = new BufferedWriter(new FileWriter(file))
    bw.write(contents)
    bw.close()
  }


}
