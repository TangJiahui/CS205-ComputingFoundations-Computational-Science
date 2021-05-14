from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import date_format
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[1]').setAppName('stock')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

text_file = spark.read.csv(
    "GOOGLE.csv", 
    header=True
)

df_with_year = text_file.withColumn("Year", date_format('Date', 'yyyy'))

df_with_year.groupBy("Year").agg({'Close':'avg'}).repartition(1).write.option("header",True) \
 .csv("output_q23")