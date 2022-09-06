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
# MAGIC 
# MAGIC 
# MAGIC ## Requirements
# MAGIC - Databricks Runtime 8.4 or above.

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

print('this is my new task')

from utils.my_func_file import my_func 

my_func()

# COMMAND ----------


