#!/usr/bin/env python

from setuptools import setup
import mlstreaming

setup(
    name='spark-ml-streaming',
    version=str(mlstreaming.__version__),
    description='A Python library for visualizing streaming machine learning in Spark',
    author='Jeremy Freeman',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/spark-ml-streaming',
    packages=['mlstreaming',
              'mlstreaming.lib'
              ],
    scripts = ['bin/streaming-kmeans'],
    package_data = {'mlstreaming.lib': ['spark-ml-streaming_2.10-' + str(mlstreaming.__version__) + '.jar']},
    install_requires=open('requirements.txt').read().split()
)