from pydantic import BaseModel
from datetime import datetime

class OrderItem(BaseModel):
    order_item_id: int
    product_name: str
    category: str
    quantity: int
    unit_price: float

class Order(BaseModel):
    order_id: int
    store_id: int
    customer_id: int
    order_date: datetime
    status: str
    payment_method: str
    delivery_address: str
    delivery_fee: float
    items: list[OrderItem]