# import mysql.connector
# import os
# from dotenv import load_dotenv
from src.db import initiate, terminate, useDB, resetDB
# import schema.orders
import pandas as pd

# Global Variables:
trial = False   # set it to true when experimenting with DB, or you may commit changes.

def display_sql(cursor, connection, database=None, table=None):
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    if database is not None:
        for i in databases:
            if database == i[0]:
                print(i, "exists!")
                if table is not None:
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    for i in tables:
                        if table == i[0]:
                            print(i, "exists!")


    else:
        for i in databases:
            print(i)
    print("--Display ended--")


def main():
    
    print("Hello from dataflow!")
    cursor, connection = useDB("dataflowDB")

    # insert_customer(cursor, connection, "Bob", "bob@example.com", "Bhopal")
    # update_customer(cursor, connection, 3, name="Bobby Deol", city="Bikaner", email="bbdeol@example.com")
    # delete_customer(cursor, connection, 2)
    
    cursor.execute("DESCRIBE products")
    print(cursor.fetchall())

if __name__ == "__main__":

    main()
