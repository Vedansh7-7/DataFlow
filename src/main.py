# import mysql.connector
# import os
# from dotenv import load_dotenv
from src.db import initiate, terminate, useDB, resetDB
import src.functions as functions
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
    # Delivered_rev = functions.revenue_status(cursor, connection)
    # Total_rev = functions.revenue_gross(cursor, connection)
    # print(f"Gross value:\t\t{Total_rev}")
    # print(f"Delivered revenue:\t{Delivered_rev}")
    # print("-"*45)
    # print(f"Difference revenue: {Total_rev - Delivered_rev}")

    # Delivered_ord = functions.orders_generated_status(cursor, connection, status='DELIVERED')
    # Cancelled_ord = functions.orders_generated_status(cursor, connection, status='CANCELLED')
    # Total_ord = functions.orders_generated_gross(cursor, connection)
    # print(f"Delivered Orders:\t{Delivered_ord}")
    # print(f"Cancelled Orders:\t{Cancelled_ord}")
    # print("-"*45)
    # print(f"Total Orders:\t\t{Total_ord}")

    # print(f"Gross AOV (Average Order Value): {functions.AOV_gross(cursor, connection):.2f}")
    # print(f"Delivered AOV: {functions.AOV_status(cursor, connection, status='DELIVERED'):.2f}")
    # print(f"Cancelled AOV: {functions.AOV_status(cursor, connection, status='CANCELLED'):.2f}")
    # print(f"Delivery rate achieved: {functions.delivery_rate(cursor, connection):.2f}")
    # print(f"Cancellation rate achieved: {functions.cancellation_rate(cursor, connection):.2f}")




if __name__ == "__main__":

    main()
