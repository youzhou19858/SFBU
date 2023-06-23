#####################################
# ratings-counter.py
#####################################

# Importing the Spark stuff that we need for Python
from pyspark import SparkConf, SparkContext
import collections
import sys

if len(sys.argv) != 2:
    raise Exception("Exactly 1 arguments are required: <inputURL>")

inputURL = sys.argv[1]

# Doing some configurations and some set up of Spark
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile(inputURL)
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

# Count up how many of each ratings type (5, 4, 3, 2, 1) exists in that dataset.
sortedResults = collections.OrderedDict(sorted(result.items()))

for key, value in sortedResults.items():
    print("%s %i" % (key, value))
