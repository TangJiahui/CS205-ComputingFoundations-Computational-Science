from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local[1]').setAppName('url')
sc = SparkContext(conf = conf)

text_file = sc.textFile("access_log")

text_file.map(lambda line: (line.split(" ")[6], 1))\
	.reduceByKey(lambda x,y: x+y)\
	.saveAsTextFile("output_q22.txt")