import pandas as pd
import sqlite3

# Connect to lesson.db (from load_db.py)
with sqlite3.connect("../db/lesson.db") as conn:
    # Load joined data into DataFrame
    query = """
        SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
    """
    df = pd.read_sql_query(query, conn)

# Preview
print("\nFirst 5 rows:")
print(df.head())

# Add total column
df["total"] = df["quantity"] * df["price"]
print("\nWith total column:")
print(df.head())

# Group by product_id
summary = df.groupby("product_id").agg({
    "line_item_id": "count",
    "total": "sum",
    "product_name": "first"
}).reset_index()

# Sort by product name
summary = summary.sort_values("product_name")

# Save to CSV
summary.to_csv("order_summary.csv", index=False)
print("\nSummary saved to order_summary.csv")
print(summary.head())
