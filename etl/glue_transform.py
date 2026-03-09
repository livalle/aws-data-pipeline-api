from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("api_etl").getOrCreate()

df = spark.read.json("s3://aws-data-lake-li/raw/")

df_clean = df.select(
    "userId",
    "id",
    "title"
)

df_clean.write.mode("overwrite").parquet(
    "s3://aws-data-lake-li/processed/posts/"
)

