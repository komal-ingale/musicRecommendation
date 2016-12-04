from pyspark import SparkContext
from pyspark.mlib.recommendation import ALS,\
  MatrixFactorizationModel 

import sys

def parseText(line):
  tokens = line.strip().split("\t")
  return (int(tokens[0]), int(tokens[1]), float(tokens[2]))

if len(sys.argv) > 4:
  
  train_file = sys.argv[1]
  test_file = sys.argv[2]
  recommendations = int(sys.argv[3])
  user_id = int(sys.argv[4])

  sc = SparkContext(appName="spark-mlib-als")
  train_set = sc.textFile(train_file).cache()
  test_set = sc.textFile(test_file)


else:
  print """I need:\
  A train set
  A test set 
  number of recommendations
  user-id"""
