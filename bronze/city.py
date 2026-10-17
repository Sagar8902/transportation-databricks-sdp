# Imprt Library

from pyspark.sql import functions as F
from pyspark import pipelines as dp

# Configration
SOURCE_DATA = "s3://cb-good-cab-002/data-source/city"


# declarative pipeline

@dp.materialized_view(
    name = 'transportation.bronze.city',
    comment = 'City Raw Data Processing',
    table_properties = {
        'quality':'bronze',
        'layer':'bronze',
        'source_format':'csv',
        'delta.enableChangeDataFeed':'true',
        'delta.autoOptimize.optimizeWrite':'true',
        'delta.autoOptimize.autoCompact':'true'
    }

)

def city_bronze():
    df = (
        spark.read
        .option('header','true')
        .option('delimiter',',')
        .option('inferSchema','true')
        .option('mergeSchema','true')
        .option('mode','PERMISSIVE')
        .option('columnNameOfCorruptRecord','_corrupt_record')
        .csv(SOURCE_DATA)
    )
        

    df =(
        df.withColumn('file_name',F.col('_metadata.file_path'))
            .withColumn('ingest_date',F.current_timestamp())
    ) 
    
    return df