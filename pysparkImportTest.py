import os
import sys

#Path for spark source folder
os.environ['SPARK_HOME'] = "/home/ronan/Documents/BigData/spark/spark-2.0.2"
os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"

#Append pyspark to Python Path
sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python")
sys.path.append("/home/ronan/Documents/BigData/spark/spark-2.0.2/python/lib/py4j-0.10.3-src")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)

sc = SparkContext('local')
words = sc.parallelize(["scala","java","hadoop","spark", "akka"])
print(words.count())
