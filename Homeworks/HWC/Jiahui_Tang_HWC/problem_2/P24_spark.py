from pyspark import SparkConf, SparkContext
import pyspark.sql.functions as sf
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[1]').setAppName('movie')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

text_file = spark.read.csv(
    "ratings.csv", 
    header=True
)

avg_df = text_file.groupBy("movieId").agg(sf.avg("rating").alias("avg_rating"))
range_df = avg_df.groupBy(sf.ceil("avg_rating").alias("Range")).agg(sf.collect_list("movieId").alias("list_of_movieId"))
changedTypedf = range_df.withColumn("list_of_movieId", range_df["list_of_movieId"].cast("string"))
changedTypedf.repartition(1).write.option("header",True).csv("output_q24")