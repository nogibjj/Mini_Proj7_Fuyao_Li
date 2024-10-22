"""Query the database"""

from databricks import sql
from dotenv import load_dotenv
import os


def insert_row(date, location, city, state, lat, lng):
    """create a new row using Databricks."""
    load_dotenv()
    databricks_key = os.getenv("DATABRICKS_KEY")
    server_host_name = os.getenv("SERVER_HOST_NAME")
    sql_http = os.getenv("SQL_HTTP")

    with sql.connect(
        access_token=databricks_key,
        server_hostname=server_host_name,
        http_path=sql_http,
    ) as connection:
        with connection.cursor() as cursor:
            insert_query = """
            INSERT INTO FL_citydb (date, location, city, state, lat, lng)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (date, location, city, state, lat, lng))
            result = cursor.fetchall()
            print(result)
        cursor.close()
        connection.close()
    return result


def update_row(city, date):
    """Update a row based on city using Databricks."""
    load_dotenv()
    databricks_key = os.getenv("DATABRICKS_KEY")
    server_host_name = os.getenv("SERVER_HOST_NAME")
    sql_http = os.getenv("SQL_HTTP")

    with sql.connect(
        access_token=databricks_key,
        server_hostname=server_host_name,
        http_path=sql_http,
    ) as connection:
        with connection.cursor() as cursor:
            update_query = """
            UPDATE FL_citydb
            SET date = ?
            WHERE city = ?;
            """
            cursor.execute(update_query, (date, city))
            result = cursor.fetchall()
            print(result)
    return result


def delete_row(city):
    """Update a row based on city using Databricks."""
    load_dotenv()
    databricks_key = os.getenv("DATABRICKS_KEY")
    server_host_name = os.getenv("SERVER_HOST_NAME")
    sql_http = os.getenv("SQL_HTTP")

    with sql.connect(
        access_token=databricks_key,
        server_hostname=server_host_name,
        http_path=sql_http,
    ) as connection:
        with connection.cursor() as cursor:
            delete_query = """DELETE FROM FL_citydb WHERE city = ?"""
            cursor.execute(delete_query, (city,))
            result = cursor.fetchall()
            print(result)
        cursor.close()
        connection.close()
    return result
