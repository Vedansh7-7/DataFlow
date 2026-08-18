from fastapi import FastAPI, HTTPException
from src import db, functions


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ram Ram!\nThis is DataFlow API"}

@app.get("/revenue")
def revenue(status='TOTAL'):
    cursor, connection = db.useDB("dataflowDB")
    if status == 'TOTAL':
        total_revenue = functions.total_revenue(cursor, connection)
        return {
            "Revenue": total_revenue
        }
    elif status in ["DELIVERED", "CANCELLED", "RETURNED", "PENDING", "OUT FOR DELIVERY"]:
            status_rev = functions.revenue_by_status(
                cursor, connection, status
            )
            return {"Orders": status_rev}
    
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid revenue status: {status}"
        )

@app.get("/order")
def order(status='DESCRIPTION'):
    cursor, connection = db.useDB("dataflowDB")
    if status == 'TOTAL':
        total_orders = functions.total_orders(cursor, connection)
        return {
            "Orders": total_orders
        }
    elif status == 'DESCRIPTION':
        desc_orders = functions.orders_describe(cursor, connection)
        return {
            "Orders": desc_orders
        }
    elif status in ["DELIVERED", "CANCELLED", "RETURNED", "PENDING", "OUT FOR DELIVERY"]:
        status_orders = functions.orders_by_status(
            cursor, connection, status
        )
        return {"Orders": status_orders}

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid order status: {status}"
        )

@app.get('/order/{order_id}')
def get_order(order_id):
    cursor, connection = db.useDB("dataflowDB")
    cursor.execute(
        """
        SELECT o.order_id, o.store_id, o.customer_id, o.order_date, o.status, o.payment_method, o.delivery_address, o.delivery_fee, oi.order_item_id, p.name, p.category, oi.quantity, oi.unit_price
        FROM orders o 
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON p.product_id = oi.product_id
        WHERE o.order_id = %s
        """,
        [order_id]
    )
    rows = cursor.fetchall()
    if not rows:
        raise HTTPException(
            status_code=404,
            detail=f"Order {order_id} not found"
        )
    else:
        #   o.order_id, o.store_id, o.customer_id, o.order_date, o.status, o.payment_method, o.delivery_address, o.delivery_fee, oi.order_item_id, p.product_name, p.category, oi.quantity, oi.unit_price
        columns_order_query = ["order id", "store id", "customer id", "order date", "status", "payment method", "delivery address", "delivery fee", "order item id", "product name", "category", "quantity", "unit price"]
        result = {}
        for idx in range(len(columns_order_query)):
            result[columns_order_query[idx]] = rows[0][idx]
        
        for row in rows:
            ...

        return rows
