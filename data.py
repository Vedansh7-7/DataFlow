import pandas as pd

customers = pd.read_csv("out/customers.csv")
order_items = pd.read_csv("out/order_items.csv")
orders = pd.read_csv("out/orders.csv")
products = pd.read_csv("out/products.csv")
stores = pd.read_csv("out/stores.csv")

list_of_dfs = [customers, order_items, orders, products, stores]
for df in list_of_dfs:
    print(df.head())
    print(df.columns)
    print(df.shape)