#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    File name: pysparkImportTest.py
    Author: Ronan Lachater
    Date created: 16/12/2017
    Date last modified: 16/12/2017
    Python Version: 3.x
'''

import os
import sys

# execute external binary files with params
# import subprocess
# subprocess.call([pyspark,--jars /home/ronan/Documents/BigData/elasticSearch/elasticsearch-hadoop-5.4.0/+\
#     dist/elasticsearch-hadoop-5.4.0.jar"])
# os.system("/home/ronan/Documents/BigData/spark/spark-2.0.2/bin/pyspark --jars /home/ronan/Documents/BigData/elasticSearch/elasticsearch-hadoop-5.4.0/+\
#     dist/elasticsearch-hadoop-5.4.0.jar")

#Path for spark source folder + connector ES/spark jar
os.environ['SPARK_HOME'] = "/home/ronan/Documents/BigData/spark/spark-2.0.2"
#Security, python3 already defined in spark conf file: spark-env.sh.template
# os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
os.environ['SPARK_CLASSPATH'] =  "/home/ronan/Documents/BigData/elasticSearch/elasticsearch-hadoop-5.4.0/dist/elasticsearch-hadoop-5.4.0.jar"
# os.environ['SPARK_CLASSPATH'] = "/home/ronan/Documents/BigData/spark/mongo-spark-connector_2.10-2.0.0.jar"
# os.environ['SPARK_CLASSPATH'] = "/home/ronan/Documents/BigData/spark/mongo-java-driver-3.0.1.jar"

#Append pyspark to Python Path
sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python")
sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python/lib/py4j-0.10.3-src")

import datetime

# Test connection
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SparkSession

    print("Successfully imported Spark Modules")

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)

# Text ES index (mongoDB admin db)
sc = SparkContext('local')
sc.setLogLevel("ERROR")




# sc.parallelize([4])
conf = { "es.resource" : "db_wine_admin/user" }
es_rdd = sc.newAPIHadoopRDD(inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
    keyClass="org.apache.hadoop.io.NullWritable",
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf=conf)

print(datetime.datetime.now())
print(es_rdd.count())
print(datetime.datetime.now())
#es_rdd.takeSample(False,10,2)
# print(es_rdd.take(5))
# mapped_rdd = es_rdd.flatMap(lambda user: user[1]['user']).count()
# print(es_rdd.first()[1]['user'][0]['city'])
# mappedCities = es_rdd.map(lambda user: user[1]['user'][0]['city']).reduce("Oslo")
# print(mappedCities.take(5))
# es_rdd.foreach(lambda user: print(user[1]['user'][order][0]))

# sparkSessionMono = SparkSession \
#     .builder \
#     .appName("PysparkMongoDB") \
#     .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/db_wine_admin.user") \
#     .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/db_wine_admin.user") \
#     .getOrCreate()
# df = sparkSessionMono.read.format("com.mongodb.spark.sql.DefaultSource").load()
# print(df)
print("process ending...")
