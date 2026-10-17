from pyspark.sql import functions as F
from pyspark import pipelines as dp

@dp.materialized_view(
    name = 'transportation.silver.city',
    comment = 'cleaned & transformed silver layer data',
    table_properties = {
        'quality':'silver',
        'layer':'silver',
        'delta.enableChangeDataFeed':'true',
        'delta.autoOptimize.optimizeWrite':'true',
        'delta.autoOptimize.autoCompact':'true'
    }

)

def city_silver():
    df_bronze = spark.read.table("transportation.bronze.city")
    df_silver = df_bronze.select(
        F.col('city_id').alias('city_id'),
        F.col('city_name').alias('city_name'),
        F.col('file_name').alias('file_name'),
        F.col('ingest_date').alias('bronze_ingest_timestamp')
    )

    df_silver = df_silver.withColumn(
                'silver_ingest_timestamp',
                F.current_timestamp()
    )

    return df_silver