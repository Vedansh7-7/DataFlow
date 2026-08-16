

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

