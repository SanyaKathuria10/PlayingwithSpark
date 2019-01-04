#Project description:
Developed a web application that extracts and discovers the trend of keywords, languages or technologies over the desired time period using the Stack Overflow data. Apart from dealing with challenges of big-data like data collection, transformation and keyword extraction, we also want to store our data in a NoSQL database and build an application which scales with user traffic.

#About the Dataset:
Dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website.

This is organized as three tables:

Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
Tags contains the tags on each of these questions

#Technologies Used :

AWS EC2
AWS Lambda
Apache Spark
Cassandra
HTML and Javascript
PySpark.

#References:
https://www.rosehosting.com/blog/how-to-install-apache-cassandra-on-ubuntu-16-04/
https://www.tutorialspoint.com/cassandra/
https://stackoverflow.com/questions/36133127/how-to-configure-cassandra-for-remote-connection
https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/module-4/
https://www.inertia7.com/projects/36
https://medium.com/ymedialabs-innovation/apache-spark-on-a-multi-node-cluster-b75967c8cb2b
https://github.com/datastax/spark-cassandra-connector/blob/master/doc/14_data_frames.md
https://stackoverflow.com/questions/29121904/cassandra-cqlsh-connection-refused
https://aws.amazon.com/blogs/big-data/from-sql-to-microservices-integrating-aws-lambda-with-relational-databases/
https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04
https://stackoverflow.com/questions/36133127/how-to-configure-cassandra-for-remote-connection
