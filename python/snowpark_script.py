import os
from snowflake.snowpark import Session

connection_parameters = {
  "account": "{{ env_var('DBT_SNOWFLAKE_ACCOUNT') }}",
  "user": "{ env_var('DBT_SNOWFLAKE_USERNAME') }}",
  "password": "{{ env_var('DBT_SNOWFLAKE_PW') }}",
  "role": "{{ env_var('DBT_SNOWFLAKE_ROLE') }}",
  "warehouse": "COMPUTE_WH",
  "database": "analytics",
  "schema": "dbt"
}


session = Session.builder.configs(connection_parameters).create()

customers = session.sql("select CUSTOMER_ID from dbt.customers")

customers.write.mode("overwrite").save_as_table("CUSTOMER_ID")