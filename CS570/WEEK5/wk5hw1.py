from pyspark import SparkContext
import sys

if len(sys.argv) != 2:
    raise Exception("Exactly 1 arguments are required: <inputURL>")

inputURL = sys.argv[1]

# Create a SparkContext
sc = SparkContext("local", "LogAnalysis")

# Read input file
inputRDD = sc.textFile(inputURL).cache()

# lines containing '[error]'
errorsRDD = inputRDD.filter(lambda x: "[error]" in x)

# lines containing "[info]"
infosRDD = inputRDD.filter(lambda x: "[info]" in x)

# lines containing "statistics:"
statisticsRDD = inputRDD.filter(lambda x: "statistics")

print(f"{errorsRDD.count()} lines of error")
print(f"{infosRDD.count()} lines of info")
print(f"{statisticsRDD.count()} lines of statistics")
print(f"{errorsRDD.count() + infosRDD.count()} lines of error and info")
print(f"{infosRDD.count() + statisticsRDD.count()} lines of info and statistics")
for line in infosRDD.take(3):
    print(line)

# Stop the SparkContext
sc.stop()
