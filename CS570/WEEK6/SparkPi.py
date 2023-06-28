from pyspark import SparkContext
import sys
from operator import add


def calculate_pi(inputURL):
    # Create a SparkContext
    sc = SparkContext("local", "PiCalculation")
    # Read input file
    inputRDD = sc.textFile(inputURL).cache()
    # calculate hits
    allPairs = inputRDD.map(lambda line: [float(x) for x in line.split(',')])
    allHits = allPairs.map(
        lambda pair: 1 if pair[0] ** 2 + pair[1] ** 2 <= 1 else 0).reduce(add)
    print(f"{allHits.count()} hits out of {allPairs.count()} draws --> Estimated Pi: {4 * allHits.count() / allPairs.count()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Exactly 1 arguments are required: <inputURL>")
    calculate_pi(sys.argv[1])
