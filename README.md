## Visualize streaming machine learning algorithms in Spark

### About
------
This Python app generates data, analyzes it in Spark Streaming, and visualizes the results with Lightning. The demos are designed for local use, but the same algorithms can run at scale on a cluster with millions of records.

### How to use
------
To run these demos, you need:

* A working installation of [Spark](http://spark.apache.org/downloads.html)
* An installation of Python with standard scientific computing libraries (NumPy, SciPy, ScikitLearn)
* A running [Lightning](http://lightning-viz.org) server

With those three things in place, set `SPARK_HOME` to your Spark installation, then start the executable:

	bin/streaming-kmeans <temporary_path> -l <lighting_host>

Where `temporary_path` is where data will be written / read, and `lightning_host` is the address of your Lightning server. After it starts, your browser will open with the visualization, and you should see data appear shortly. 

Try running with different settings:

	bin/streaming-kmeans <temporary_path> -l <lighting_host> -nc <n_clusters> -hl <half_life>

To see all options type:

	bin/streaming-kmeans -h

### Build
---------------
The demo relies on a Scala package, which is included pre-built inside `python/lib`. To rebuild it, use sbt:

	cd scala
	sbt package
