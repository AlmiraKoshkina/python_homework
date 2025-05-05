import sqlite3

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# --------------------------
# Task 2: Total price of 5 orders
# --------------------------
print("== Task 2: First 5 Orders and Total Price ==")
cursor.execute("""
SELECT o.order_id, 
       SUM(p.price * l.quantity) AS total_price
FROM orders AS o
JOIN line_items AS l ON o.order_id = l.order_id
JOIN products AS p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
""")
for order_id, total in cursor.fetchall():
    print(f"Order ID: {order_id}, Total: ${total:.2f}")

# --------------------------
# Task 3: Insert new order with transaction
# --------------------------
print("\n== Task 3: Create New Order with 5 Products ==")
try:
    cursor.execute("""
    INSERT INTO orders (customer_id, employee_id)
    VALUES (7, 3)
    RETURNING order_id;
    """)
    order_id = cursor.fetchone()[0]

    cursor.executemany("""
    INSERT INTO line_items (order_id, product_id, quantity)
    VALUES (?, ?, ?);
    """, [
        (order_id, 23, 10),
        (order_id, 18, 10),
        (order_id, 43, 10),
        (order_id, 9, 10),
        (order_id, 44, 10)
    ])
    conn.commit()

    # Show the line items just inserted
    cursor.execute("""
    SELECT l.line_item_id, l.quantity, p.product_name
    FROM line_items AS l
    JOIN products AS p ON l.product_id = p.product_id
    WHERE l.order_id = ?;
    """, (order_id,))
    for line_item_id, qty, name in cursor.fetchall():
        print(f"LineItem ID: {line_item_id}, Quantity: {qty}, Product: {name}")

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)



# --------------------------
# Task 4: Employees with more than 5 orders
# --------------------------
print("\n== Task 4: Employees with More Than 5 Orders ==")

cursor.execute("""
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
""")

for emp_id, first, last, count in cursor.fetchall():
    print(f"ID: {emp_id}, Name: {first} {last}, Orders: {count}")


conn.close()