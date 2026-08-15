# import mysql.connector
# import os
# from dotenv import load_dotenv
from init import initiate, terminate, useDB
import orders

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
    
    items = [
        (1, 100000),   # 2 × Milk
        (2, 1),   # 1 × Bread
        (3, 3)    # 3 × Eggs
    ]

    try:
        order_id = orders.create_order(
            cursor,
            customer_id=3,
            store_id=1,
            payment_method="UPI",
            address="Vijay Nagar, Indore",
            items=items
        )

        connection.commit()
        print("Order created:", order_id)

    except Exception as e:
        connection.rollback()
        print("Order failed:", e)

if __name__ == "__main__":

    main()
