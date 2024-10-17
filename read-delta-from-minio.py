from pyspark.sql import SparkSession

# Replace these values with your MinIO configuration
minio_access_key = "N1a96Y3vfdsfdsfdsfsdfdsOa"
minio_secret_key = "lch9rNXRfdsfdsfdsfdsfdsfdsfdsV18umhYgmKnwGWaCD"
minio_endpoint = "http://130.1.1.1:9000"  # Example: http://localhost:9000
input_bucket = "s3a://spark-delta-lake/non-partition" # Replace with your desired input  path in MinIO

# Create a Spark session with the necessary MinIO/S3A configurations
spark = SparkSession.builder \
    .appName("ReadDeltaToMinIO") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.hadoop.fs.s3a.access.key", minio_access_key) \
    .config("spark.hadoop.fs.s3a.secret.key", minio_secret_key) \
    .config("spark.hadoop.fs.s3a.endpoint", minio_endpoint) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
    .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore") \
    .getOrCreate()


# Read DataFrame from Delta format on MinIO
df = spark.read.format("delta").load(input_bucket)

# Show the DataFrame
df.show()

# Stop Spark Session
spark.stop()
