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

def terminate(cursor, connection):
    cursor.close()
    connection.close()


def main():
    
    print("Hello from dataflow!")
    cursor, connection = initiate()
    terminate(cursor, connection)
    


if __name__ == "__main__":
    main()
