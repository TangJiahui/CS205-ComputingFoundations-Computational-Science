from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[3]", "NetworkWordCount") # local streaming context
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 5) # batch interval of 1 second

lines = ssc.socketTextStream("localhost", 9999) # create DStream; connect to localhost:9999

words = lines.flatMap(lambda line: line.split(" ")) # Split the lines into words

# Count each word in each batch
pairs = words.map(lambda word: (word, 1)) # create (K,V) pairs of words and the number 1
wordCounts = pairs.reduceByKey(lambda x, y: x + y) # count those words

wordCounts.pprint() # print first 10 elements of each RDD generated in this DStream

ssc.start() # start the computation
ssc.awaitTermination() # wait for it to finish
