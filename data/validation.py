import src.db as db

cursor, connection = db.useDB("dataflowDB")
print("Checking for orphaned orders (orders without valid customers)...")
cursor.execute(
    """
    SELECT COUNT(*)
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    WHERE c.customer_id IS NULL
    """
)

print(f"# of such orders = {cursor.fetchone()[0]}\n\nChecking for order items without real products...")

cursor.execute(
    """
    SELECT COUNT(*)
    FROM order_items oi
    LEFT JOIN products p ON oi.product_id = p.product_id
    WHERE p.product_id IS NULL
    """
)


print(f"# of such order items = {cursor.fetchone()[0]}\n\nChecking for orders without order items...")

cursor.execute(
    """
    SELECT COUNT(*)
    FROM orders o
    LEFT JOIN order_items oi ON o.order_id = oi.order_id
    WHERE oi.order_id is NULL
    """
)

print(f"# of such orders = {cursor.fetchone()[0]}\n\nChecking for products without stores...")

cursor.execute(
    """
    SELECT COUNT(*)
    FROM products p
    LEFT JOIN stores s ON p.store_id = s.store_id
    WHERE s.store_id is null
    """
)

print(f"# of such products = {cursor.fetchone()[0]}\n\nChecking for duplicate customers_ids in customers table...")

cursor.execute(
    """
    SELECT customer_id, COUNT(*)
    FROM customers
    GROUP BY customer_id
    HAVING COUNT(*) > 1
    """
)

duplicates = cursor.fetchall()
print(f"# of such duplicate customer_ids = {len(duplicates)}\n\nChecking for duplicate customers (same name, email, and city)...")

cursor.execute(
    """
    SELECT name, email, city, COUNT(*)
    FROM customers
    GROUP BY name, email, city
    HAVING COUNT(*) > 1
    """
)

duplicates = cursor.fetchall()
print(f"# of such duplicate customers = {len(duplicates)}\n\nChecking for NULLs in critical columns...")
cursor.execute(
    """
    SELECT COUNT(*)
    FROM customers
    WHERE name IS NULL OR email IS NULL OR city IS NULL
    """
)
count_of_nulls = {}
count_of_nulls["customers"] = cursor.fetchall()[0][0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM products
    WHERE name IS NULL OR price IS NULL OR store_id IS NULL
    """
)

count_of_nulls["products"] = cursor.fetchall()[0][0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM orders
    WHERE customer_id IS NULL OR order_date IS NULL
    """
)

count_of_nulls["orders"] = cursor.fetchall()[0][0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM order_items
    WHERE order_id IS NULL OR product_id IS NULL OR quantity IS NULL
    """
)

count_of_nulls["order_items"] = cursor.fetchall()[0][0]

print(f"Count of NULLs in critical columns: {count_of_nulls}")

print("\nChecking for negative prices in products table...")

cursor.execute(
    """
    SELECT COUNT(*) FROM products
    WHERE price < 0
    """
)

print(f"# is: {cursor.fetchall()[0][0]}")

print("\nChecking for negative stocks in products table...")

cursor.execute(
    """
    SELECT COUNT(*) FROM products
    WHERE stock < 0;
    """
)


print(f"# is: {cursor.fetchall()[0][0]}")

print("\nChecking invalid order status: ")
cursor.execute(
    """
    SELECT COUNT(*)
    FROM orders
    WHERE status NOT IN (
        'DELIVERED',
        'CANCELLED',
        'RETURNED',
        'PENDING',
        'OUT_FOR_DELIVERY'
    );
    """
)

print(cursor.fetchall()[0][0])


print("\nChecking invalid order quantities...")

cursor.execute(
    """
    SELECT COUNT(*)
    FROM order_items
    WHERE quantity <= 0;
    """
)

print("We got", cursor.fetchall()[0][0], "ambigious orders.")

print("\nChecking invalid order item prices...")

cursor.execute(
    """
    SELECT COUNT(*)
    FROM order_items
    WHERE unit_price < 0;
    """
)

print(f"We got {cursor.fetchall()[0][0]} items in order_items.")