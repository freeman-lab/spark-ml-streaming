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

	streaming-kmeans <temporary_path> -l <lighting_host>

Where `temporary_path` is where data will be written / read, and `lightning_host` is the address of your Lightning server. After it starts, your browser will open, and you should see data appear shortly. 

Try running with different settings, for example, to run a 1-d version with 4 clusters and a half-life of 3 batches:

	bin/streaming-kmeans <temporary_path> -l <lighting_host> -nc 4 -nd 1 -hl 3 -tu batches

To see all options type:

	bin/streaming-kmeans -h

2-d data will make a scatter plot and 1-d data will make a line plot.

### Build
The demo relies on a Scala package included pre-built inside `python/lib`. To rebuild it, use sbt:

	cd scala
	sbt package
