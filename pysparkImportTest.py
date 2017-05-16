#!/usr/bin/python
import os
import sys

import subprocess
# subprocess.call([pyspark,--jars /home/ronan/Documents/BigData/elasticSearch/elasticsearch-hadoop-5.4.0/+\
#     dist/elasticsearch-hadoop-5.4.0.jar"])
# os.system("/home/ronan/Documents/BigData/spark/spark-2.0.2/bin/pyspark --jars /home/ronan/Documents/BigData/elasticSearch/elasticsearch-hadoop-5.4.0/+\
#     dist/elasticsearch-hadoop-5.4.0.jar")

#Path for spark source folder
# os.environ['SPARK_HOME'] = "/home/ronan/Documents/BigData/spark/spark-2.0.2"
# os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"

#Append pyspark to Python Path
# sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python")
# sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python/lib/py4j-0.10.3-src")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)

sc = SparkContext('local')
conf = { "es.resource" : "db_wine_admin/user" }
es_rdd = sc.newAPIHadoopRDD(inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
    keyClass="org.apache.hadoop.io.NullWritable",
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf=conf)
print(es_rdd.first())
