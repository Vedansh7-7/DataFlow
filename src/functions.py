def delivery_rate(cursor, connection):
    return (orders_by_status(cursor, connection, status='DELIVERED') / total_orders(cursor, connection)) * 100


def cancellation_rate(cursor, connection):
    return (orders_by_status(cursor, connection, status='CANCELLED') / total_orders(cursor, connection)) * 100


def revenue_by_status(cursor, connection, status='DELIVERED'):
    cursor.execute(
        """
        SELECT SUM(oi.quantity * oi.unit_price) AS Revenue
        FROM order_items oi
        INNER JOIN orders o ON oi.order_id = o.order_id
        WHERE o.status = %s
        """,
        [status]
    )

    return cursor.fetchall()[0][0]


def total_revenue(cursor, connection):
    cursor.execute(
        """
        SELECT SUM(oi.quantity * oi.unit_price) AS Revenue
        FROM order_items oi
        """
    )

    return cursor.fetchall()[0][0]


def orders_by_status(cursor, connection, status='DELIVERED'):
    cursor.execute(
        """
        SELECT COUNT(*) AS Total_orders
        FROM orders
        WHERE status = %s
        """,
        [status]
    )

    return cursor.fetchall()[0][0]


def total_orders(cursor, connection):
    cursor.execute(
        """
        SELECT COUNT(*) AS Total_orders
        FROM orders
        """
    )

    return cursor.fetchall()[0][0]


def AOV_gross(cursor, connection):
    return total_revenue(cursor, connection) / total_orders(cursor, connection)


def AOV_by_status(cursor, connection, status='DELIVERED'):
    return revenue_by_status(cursor, connection, status) / orders_by_status(cursor, connection, status)