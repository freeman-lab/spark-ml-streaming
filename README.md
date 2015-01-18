Demo streaming machine learning algorithms in Spark.

This Python app generates data in Python, analyzes it in Spark Streaming, and visualizes the results with Lightning. The demos are designed for local use, but the exact same algorithms can run at scale on a cluster with millions of records.

To run these demos, you need:

* A working installation of [Spark]('http://spark.apache.org/downloads.html')
* An installation of Python with standard scientific computing libraries (NumPy, SciPy, ScikitLearn)
* A running [Lightning]('http://lightning-viz.org') server

With those three things in place, just follow these steps:

* Set SPARK_HOME to your Spark installation
* Call an executable from within the top-level directory, as in:

	bin/streaming-kmeans <temporary_path> -l <lighting_host>

Where `temporary_path` is a path where data files will be written and read from, and `lightning_host` is the address of your Lightning server. As soon as it starts your browser will open with the running visualization, and you should see data appear shortly. 

Try running with different settings:

	bin/streaming-kmeans <temporary_path> -l <lighting_host> -nc <n_clusters> -np <n_points> -hl <half_life>

And to see all options type:

	bin/streaming-kmeans -h

The demo relies on a Scala package, which is included pre-built inside `python/lib` and used by default. If you want to rebuild it, use sbt:

	cd scala
	sbt package