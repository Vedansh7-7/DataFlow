

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
            SELECT price, stock, store_id
            FROM products
            WHERE product_id = %s
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            raise ValueError(f"Product {product_id} does not exist")

        price, stock, product_store_id = product

        if product_store_id != store_id:
            raise ValueError(
                f"Product {product_id} does not belong to store {store_id}"
            )

        if stock < quantity:
            raise ValueError(
                f"Insufficient stock for product {product_id}"
            )

        cursor.execute(
            """
            INSERT INTO order_items
                (order_id, product_id, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
            """,
            (order_id, product_id, quantity, price)
        )

        cursor.execute(
            """
            UPDATE products
            SET stock = stock - %s
            WHERE product_id = %S
            """,
            (quantity, product_id)
        )

    return order_id
