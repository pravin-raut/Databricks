# Databricks notebook source
# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.help("mount")

# COMMAND ----------

dbutils.fs.mount(source,mountpoint,extraconfig)

# COMMAND ----------

#storage Account Name : fsmstorageaccountdemo
#Container Name : fsminputdataset

#/mnt/fsmdataset
dbutils.fs.mount(
source = 'wasbs://fsminputdataset@fsmstorageaccountdemo.blob.core.windows.net',
mount_point='/mnt/fsmdataset',
extra_configs={'fs.azure.account.key.fsmstorageaccountdemo.blob.core.windows.net':'0C0SyGjbNqaHb8t6l4PINKAvWPOaTMUFmmqcj3jC9q2UeaXKv5LgTUlWgu6E0Ce7uu9V2gjhMaL4+AStS3lEzQ=='}
)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/mnt/fsmdataset
