[![Join the chat at https://gitter.im/freeman-lab/spark-ml-streaming](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/freeman-lab/spark-ml-streaming?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Visualize streaming machine learning in Spark

![two-dimensional-demo](https://github.com/freeman-lab/spark-streaming-demos/blob/master/animations/databricks-blog-post/4-five-clusters.gif)
![one-dimensional-demo](https://github.com/freeman-lab/spark-streaming-demos/blob/master/animations/databricks-blog-post/6-half-life-5p0.gif)

### About
This Python app generates data, analyzes it in Spark Streaming, and visualizes the results with Lightning. The analyses use streaming machine learning algorithms included with Spark as of version 1.2. The demos are designed for local use, but the same algorithms can run at scale on a cluster with millions of records.

### How to use
To run these demos, you need:

* A working installation of [Spark](http://spark.apache.org/downloads.html)
* A running [Lightning](http://lightning-viz.org) server
* An installation of Python with standard scientific computing libraries (NumPy, SciPy, ScikitLearn)

With those three things in place, install using:

	pip install spark-ml-streaming

Then set `SPARK_HOME` to your Spark installation, and start an executable:

	streaming-kmeans -l <lighting_host>

Where `lightning_host` is the address of your Lightning server. After it starts, your browser will open, and you should see data appear shortly. 

Try running with different settings, for example, to run a 1-d version with 4 clusters and a half-life of 10 points:

	streaming-kmeans -p <temporary_path> -l <lighting_host> -nc 4 -nd 1 -hl 10 -tu points

Where `temporary_path` is where data will be written / read, if not specified the current tmp directory will be used (See Python [tempfile.gettempdir()](https://docs.python.org/2/library/tempfile.html))

2D data will make a scatter plot and 1D data will make a line plot. You can set this with -nd.

To see all options type:

	streaming-kmeans -h

### Build
The demo relies on a Scala package included pre-built inside `python/mlstreaming/lib`. To rebuild it, use sbt:

	cd scala
	sbt package
