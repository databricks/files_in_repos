# Databricks notebook source
# MAGIC %md # Working with files in Databricks Repos
# MAGIC This notebook shows how you can work with arbitrary files in Databricks Repos. Some common use cases are:
# MAGIC - Custom Python and R modules. When you include these modules in a repo, notebooks in the repo can access their functions using an `import` statement.
# MAGIC - Define an environment in a `requirements.txt` file in the repo. Then just run `pip install -r requirements.txt` from a notebook to install the packages and create the environment for the notebook.
# MAGIC - Include small data files in a repo. This can be useful for development and unit testing. The maximum size for a data file in a repo is 100 MB. Databricks Repos provides an editor for small files (< 10 MB).
# MAGIC 
# MAGIC ## How to use this notebook
# MAGIC To use this notebook, clone this repo ([AWS](https://docs.databricks.com/repos.html#clone-a-remote-git-repository)|[Azure](https://docs.microsoft.com/azure/databricks/repos#clone-a-remote-git-repository)|[GCP](https://docs.gcp.databricks.com/repos.html#clone-a-remote-git-repository)) into your workspace: 
# MAGIC - https://github.com/databricks/files_in_repos

# COMMAND ----------

# MAGIC %md ## Work with Python modules 
# MAGIC The current working directory (`/Workspace/Repos/<username>/<repo_name>`) is automatically included in the Python path. You can import any module in the current directory or subdirectories.

# COMMAND ----------

# Print the path
import sys
print("\n".join(sys.path))

# COMMAND ----------

from sample import n_to_mth
n_to_mth(3, 4)

# COMMAND ----------

from utils.sample2 import cube_root
cube_root(8)

# COMMAND ----------

# MAGIC %md To import modules from other repositories, add them to the Python path.  
# MAGIC For example, if you have a repo named `supplemental_files` with a Python module `lib.py`, you can import it as shown in the next cell.

# COMMAND ----------

import sys
import os

# In the command below, replace <username> with your Databricks user name.
sys.path.append(os.path.abspath('/Workspace/Repos/<username>/supplemental_files'))

# You can now import Python modules from the supplemental_files repo.
# import lib

# COMMAND ----------

# MAGIC %md ## Automatic reload
# MAGIC 
# MAGIC Suppose you edited `sample.py` to add a function `rectangle` to calculate the area of a rectangle. You can run the commands below to automatically reload the module.

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# For this command to work, you must edit the file `sample.py` and add this function:
# def rectangle(a, b):
#    return a * b

# Then, execute this cell.
from sample import rectangle
rectangle(5, 4)

# COMMAND ----------

# MAGIC %md ## Install packages from `requirements.txt` file

# COMMAND ----------

pip install -r requirements.txt

# COMMAND ----------

# MAGIC %md  ## Work with small data files
# MAGIC You can include small data files in a repo, which is useful for development and unit testing. The maximum size for a data file in a repo is 100 MB. Databricks Repos provides an editor for small files (< 10 MB).
# MAGIC You can read in data files using Python, shell commands, pandas, Koalas, or PySpark.

# COMMAND ----------

# MAGIC %md ### View file with Python

# COMMAND ----------

import csv
with open('data/winequality-red.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# COMMAND ----------

# MAGIC %md ### View file with shell commands

# COMMAND ----------

# MAGIC %sh head -10 data/winequality-red.csv

# COMMAND ----------

# MAGIC %md ### Load file with pandas

# COMMAND ----------

import pandas as pd

df= pd.read_csv("data/winequality-red.csv")
display(df)

# COMMAND ----------

# MAGIC %md ### Load file with Koalas
# MAGIC Koalas requires the absolute file path.

# COMMAND ----------

import os
import databricks.koalas as ks

df= ks.read_csv(f"file:{os.getcwd()}/data/winequality-red.csv") # "file:" prefix and absolute file path are required for Koalas
display(df)

# COMMAND ----------

# MAGIC %md ### Load file with PySpark
# MAGIC PySpark requires the absolute file path.

# COMMAND ----------

import os

df=spark.read.csv(f"file:{os.getcwd()}/data/winequality-red.csv", header=True) # "file:" prefix and absolute file path are required for PySpark
display(df)

# COMMAND ----------

# MAGIC %md ## Limitations
# MAGIC You cannot programmatically write to a file.
