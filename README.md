# How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

I've playing for a while changing and adding some paramters described  in https://spark.apache.org/docs/latest/configuration.html.
My first configuration was pretty basic, tunnig the parameters I was able to improve the thoughput and latency of the spark job, sometimes they affect the performance positevely, others negatively and sometimes the changes didn't make an impact.

# What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
changing the parameter maxOffsetsPerTrigger to 5000 gives me better permormance moving from 8-10 rows per seconds to around 300.

I also played with other parameters like maxRatePerPartition, spark.sql.shuffle.partitions and spark.executor.cores but I didn't see much impact.


