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

def logIt():
    ...
        

def terminate(cursor, connection):
    cursor.close()
    connection.close()