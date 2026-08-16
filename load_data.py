import pandas as pd
from init import terminate, useDB

def load_csv(cursor, connection, table, csv_path, columns):
    df = pd.read_csv(csv_path)

    data = df[columns].values.tolist()
    column_string = ", ".join(columns)
    value_placeholders = ", ".join(["%s"] * len(columns))

    cursor.executemany(
        f"""
        INSERT INTO {table}
            ({column_string})
        VALUES ({value_placeholders})
        """,
        data
    )

    connection.commit()

    print(f"Inserted {cursor.rowcount} rows into table.\nLoaded {len(data)} roww")

def main():
    cursor, connection = useDB("dataflowDB")

    try:
        load_csv(
            cursor,
            connection,
            "order_items",
            "out/order_items.csv",
            [
                "order_item_id",
                "order_id",
                "product_id",
                "quantity",
                "unit_price"
            ]
        )

    except Exception as e:
        connection.rollback()
        print(f"Loading failed, error occurred: {e}")

    finally:
        terminate(cursor, connection)

if __name__ == "__main__":
    main()