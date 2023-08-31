# Databricks notebook source
import os

current_working_dir = os.getcwd()
current_working_dir

# COMMAND ----------

df = spark.read.format("csv").option("header", "true").option("delimiter", ";").load(f"file://{current_working_dir}/sample.csv")
display(df)

# COMMAND ----------

import pandas as pd

# example
pd.read_csv("/Workspace/Repos/pawarit.laosunthara@databricks.com/files_in_repos/sample.csv", sep=";")

# COMMAND ----------

import pandas as pd

# you should be able to read arbitrary files using any functions/libraries in the Python ecosystem
pandas_df = pd.read_csv(f"{current_working_dir}/sample.csv", sep=";")
pandas_df

# COMMAND ----------

spark_df = spark.createDataFrame(pandas_df)
display(spark_df)

# COMMAND ----------

with open("./LICENSE.txt", "r") as f:
  print(f.read()) # another example: read some arbitrary text
