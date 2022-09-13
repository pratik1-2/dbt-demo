import os
from snowflake.snowpark import Session

# DBT_SNOWFLAKE_ACCOUNT = os.environ['DBT_SNOWFLAKE_ACCOUNT']
# DBT_SNOWFLAKE_USERNAME = os.environ['DBT_SNOWFLAKE_USERNAME']
# DBT_SNOWFLAKE_PW = os.environ['DBT_SNOWFLAKE_PW']
# DBT_SNOWFLAKE_ROLE = os.environ['DBT_SNOWFLAKE_ROLE']
connection_parameters = {
  "account": os.environ['DBT_SNOWFLAKE_ACCOUNT'],
  "user": os.environ['DBT_SNOWFLAKE_USERNAME'],
  "password": os.environ['DBT_SNOWFLAKE_PW'],
  "role": os.environ['DBT_SNOWFLAKE_ROLE'],
  "warehouse": "COMPUTE_WH",
  "database": "analytics",
  "schema": "dbt"
}


session = Session.builder.configs(connection_parameters).create()

customers = session.sql("select CUSTOMER_ID from dbt.customers")

customers.write.mode("overwrite").save_as_table("CUSTOMER_ID")