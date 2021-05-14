from pyspark import SparkConf, SparkContext
import sys
import re

pattern = re.compile(sys.argv[1])


conf = SparkConf().setMaster('local[1]').setAppName('grep')
sc = SparkContext(conf = conf)

text_file = sc.textFile("input.txt")

text_file.filter(lambda line: re.search(pattern, line)).saveAsTextFile("output_q21.txt")