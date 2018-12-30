from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import SparseVector
import sys
from operator import add
import pandas as pd
from pyspark.sql import functions as F
from itertools import islice
import pyspark_cassandra
from pyspark_cassandra import CassandraSparkContext
from cassandra.cluster import Cluster
#import org.apache.spark.sql.cassandra._
#import com.datastax.spark.connector.cql.CassandraConnectorConf
#import com.datastax.spark.connector.rdd.ReadConf
 
#with open("AnswersOutput.csv") as myFile:
#	head = list(isslice(myFile, 1000))
#print 
#import org.apache.spark.SparkContext
#import org.apache.spark.SparkConf
#from sklearn.feature_extractiom
conf = SparkConf().setMaster("local").setAppName("Simple Application")
#.set("spark.cassandra.connection.host","172.31.87.203")
sc = SparkContext(conf= conf)

sqlContext = SQLContext(sc)
#pandas_df = pd.read_csv('AnswersOutput.csv').head(30)
spak = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

#output = counts.collect()
#for (word, count) in output:
#       print("%s: %i" % (word, count))
#lines.select(F.date_format('timestamp','yyyy-MM-dd').alias('day')).groupby('day').show()
#textfile = sc.textFile("abc.csv");
#splitrdd = textfile.map(lambda line:line.split(" "))
#print splitrdd
#output = splitrdd.collect()
data = spak.read.text("AnsOutput.csv").cache()
import unicodedata
#hashmap = {"java":0,"c":1, "c++":2, "python":3}
hashmap = {"java":0,"c":1, "c++":2, "python":3,"perl":4,"sql":5,"jquery":6,"javascript":7,"html":8,"linux":9,"algorithm":10}
def someFunction(row):
    count = [0] * len(hashmap)
    print row
    wordlist = []
    data = row[0].split(" ")
    wordlist = data[1:]
    date = data[0].split("T")[0].split(",")[1]
    print wordlist
    result = list()
    for word in wordlist:
	word = str(word)
	if word in hashmap:
            count[hashmap[word]] = 1
    return date,count
def tupleCreate(list1):
   temp = []
   print list1
   #for i in range(0,len(list1)):
   for key,value in hashmap.items():
	if list1[1][value]!=0:
	  tempTuple = (list1[0],key,list1[1][value])
	  temp.append(tempTuple)
     
   return temp

def sumArrays(list1,list2):
   return list(map(add, list1, list2))
ans = data.rdd.map(someFunction).reduceByKey(sumArrays).map(tupleCreate).collect()
print ans
dataToPut = [x for x in ans if x!=[]]
print dataToPut
flat_list = [item for sublist in dataToPut for item in sublist]
print flat_list
#print ans.rdd.map(tupleCreate)
#def tupleCreate(list1):
#   temp = []
#   for i in len(list1):
#     print list1[i]

print type(flat_list)
collection = sc.parallelize(flat_list)
print collection	
#collection.saveToCassandra("stackoverflowdb","keywords_count")
cluster = Cluster(['172.31.87.203'])
session = cluster.connect('stackoverflowdb')
for i in range(len(flat_list)):
	session.execute("INSERT INTO keywords_count(timestamp, keyword, count) VALUES(%s, %s,  %s)", flat_list[i])

#print(pandas_df)
#input = sc.textFile("abc.csv")
#stopWordsInput = sc.textFile("stopwords.txt")
#stopWords = stopWordsInput.flatMap(x=> x.split("\t")).map(_.trim)
#broadcastStopWords = sc.broadcast(stopWords.collect.toSet)
#wordsWithStopWords: RDD[String] = input.flatMap(x => x.split("\\W+"
#lines = sc.read.text('abc.csv').rdd.map(lambda r: r[0])
#print(lines)
#flat_list.write.format("org.apache.spark.sql.cassandra").save()
#flat_list.setCassandraConf(CassandraConnectorConf.KeepAliveMillisParam.option(10000))


#spark.setCassandraConf("Cluster1", CassandraConnectorConf.ConnectionHostParam.option("172.31.88.166") ++ CassandraConnectorConf.ConnectionPortParam.option(12345))
sc.stop()
