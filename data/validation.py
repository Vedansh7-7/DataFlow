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

print(f"# of such products = {cursor.fetchone()[0]}")