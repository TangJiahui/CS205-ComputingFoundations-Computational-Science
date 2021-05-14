from pyspark import SparkConf, SparkContext
import sys
import re


conf = SparkConf().setAppName('grep')
sc = SparkContext(conf = conf)

text_file = sc.textFile("ratings.csv")

text_file.filter(lambda line: "5.0" in line).saveAsTextFile("output_q26.txt")