from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import date_format
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[1]').setAppName('meterite')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

text_file = spark.read.csv(
    "Meteorite_Landings.csv", 
    header=False,
).toDF("name","id","nametype","recclass","mass (g)","fall","year","reclat","reclong","GeoLocation")

text_file.groupBy("recclass").agg({'mass (g)':'avg'}).repartition(1).write.option("header",True) \
 .csv("output_q25")