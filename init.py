import mysql.connector
import os
from dotenv import load_dotenv

def initiate():
    load_dotenv()
    print("Initiating main-DB:\n")
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = os.getenv("pass")
    )
    print("Connected !")

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS dataflowDB")
    print("Database initiated !")

    return cursor, connection

def useDB(database="dataflowDB"):
    load_dotenv()
    print(f"Using {database}-as-DB:\n")
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database=database,
        password = os.getenv("pass")
    )
    print("Connected !")

    cursor = connection.cursor()
    print("Database active!")

    return cursor, connection

def resetDB(cursor, connection):
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    try:
        cursor.execute("TRUNCATE TABLE order_items")
        cursor.execute("TRUNCATE TABLE orders")
        cursor.execute("TRUNCATE TABLE products")
        cursor.execute("TRUNCATE TABLE stores")
        cursor.execute("TRUNCATE TABLE customers")
        
    except Exception as e:
        print(f"Error occurred while resetting the database: {e}")
        
    finally:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        connection.commit()

def logIt():
    ...
        

def terminate(cursor, connection):
    cursor.close()
    connection.close()