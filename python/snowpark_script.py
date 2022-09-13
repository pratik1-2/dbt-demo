import os
from snowflake.snowpark import Session

connection_parameters = {
  "account": "qb81222.ap-southeast-1",
  "user": "transform_user",
  "password": "Transform_password@11",
  "role": "TRANSFROM_ROLE",
  "warehouse": "COMPUTE_WH",
  "database": "analytics",
  "schema": "dbt"
}

session = Session.builder.configs(connection_parameters).create()

customers = session.sql("select CUSTOMER_ID from dbt.customers")

customers.write.mode("overwrite").save_as_table("CUSTOMER_ID")