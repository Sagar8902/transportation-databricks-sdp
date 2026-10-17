from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_PATH = "s3://cb-good-cab-002/data-source/trips"

@dp.table(
    name = 'transportation.bronze.trips',
    comment = 'Streaming ingestion of raw order data with Auto Loader',
    table_properties = {
        'quality':'bronze',
        'layer':'bronze',
        'source_format':'csv',
        'delta.enableChangeDataFeed':'true',
        'delta.autoOptimize.optimizeWrite':'true',
        'delta.autoOptimize.autoCompact':'true'
    }

)

def order_bronze():
    df = (
        spark.readStream.format("cloudFiles")
        .option('cloudFiles.format','csv')
        .option('cloudFiles.inferColumnTypes','true')
        .option('cloudFiles,schemaEvolutionMode','rescue')
        .option('cloudFiles.maxFilesPerTrigger',100)
        .load(SOURCE_PATH)
    )

    # Rename the problematic column

    df = df.withColumnRenamed(
        'distance_travelled(km)',
        'distance_travelled_km'
    )

    df = df.withColumn(
        'ingest_datetime',F.current_timestamp()
    )

    return df