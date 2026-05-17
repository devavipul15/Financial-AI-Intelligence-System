from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("FraudDetectionStreaming")     .getOrCreate()

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "transactions")     .load()

query = df.writeStream     .outputMode("append")     .format("console")     .start()

query.awaitTermination()