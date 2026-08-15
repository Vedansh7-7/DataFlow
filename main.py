# import mysql.connector
# import os
# from dotenv import load_dotenv
from init import initiate, terminate, useDB

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

def insert_customer(cursor, connection, name, email, city):
    # name = "Bob"
    # email = "bob@example.com"
    # city = "Bhopal"

    cursor.execute(
        """
        INSERT INTO customers (name, email, city)
        VALUES (%s, %s, %s)
        """,
        (name, email, city)
    )

    # if not trial:
    #     connection.commit()

def update_customer(cursor, connection, customer_id, **kwargs):
    if not kwargs:
        return
    ALLOWED_LIST = {"name", "email", "city"}
    set_parts = []
    values = []

    for col, val in kwargs.items():
        if col in ALLOWED_LIST:
            set_parts.append(f"{col} = %s")
            values.append(val)
    values.append(customer_id)
    if set_parts:
        cursor.execute(
            f"""
            UPDATE customers
            SET {", ".join(set_parts)}
            WHERE customer_id = %s
            """,
            values
        )
    else:
        print("No valid columns were provided!")
    # if not trial:
    #     connection.commit()

def delete_customer(cursor, connection, customer_id):
    cursor.execute(
        """
        DELETE FROM customers
        WHERE customer_id = %s
        """,
        (customer_id,)
    )

def create_order(cursor, customer_id, store_id, payment_method, address, items):

    cursor.execute(
        """
        INSERT INTO orders
            (customer_id, store_id, payment_method, delivery_address)
        VALUES (%s, %s, %s, %s)
        """,
        (customer_id, store_id, payment_method, address)
    )

    order_id = cursor.lastrowid

    for product_id, quantity in items:

        cursor.execute("""
            SELECT price, stock
            FROM products
            WHERE product_id = %s
        """, (product_id,))

        product = cursor.fetchone()

        if (product[1] - quantity >= 0):
            cursor.execute(
                """
                INSERT INTO order_items
                    (order_id, product_id, quantity, unit_price)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, product_id, quantity, product[0])
            )
        else:
            return -1

    return order_id

def main():
    
    print("Hello from dataflow!")
    cursor, connection = useDB("dataflowDB")

    # insert_customer(cursor, connection, "Bob", "bob@example.com", "Bhopal")
    # update_customer(cursor, connection, 3, name="Bobby Deol", city="Bikaner", email="bbdeol@example.com")
    # delete_customer(cursor, connection, 2)
    
    items = [
        (1, 2),   # 2 × Milk
        (2, 1),   # 1 × Bread
        (3, 3)    # 3 × Eggs
    ]

    order_id = create_order(
        cursor,
        customer_id=3,
        store_id=1,
        payment_method="UPI",
        address="Vijay Nagar, Indore",
        items=items
    )

    connection.commit()

    print("Order created:", order_id)

if __name__ == "__main__":

    main()
