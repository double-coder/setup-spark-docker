from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("VSCode Notebook") \
    .master("spark://spark-master:7077") \
    .config("spark.driver.host", "devcontainer") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")