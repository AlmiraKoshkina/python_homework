import sqlite3
import os

os.makedirs("../db", exist_ok=True)

try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
    """)

    # Insert data
    def add_publisher(name):
        cursor.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))

    def add_magazine(name, publisher_name):
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()
        if result:
            cursor.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, result[0]))

    def add_subscriber(name, address):
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

    def add_subscription(subscriber_name, magazine_name, expiration_date):
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        sub = cursor.fetchone()
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        mag = cursor.fetchone()
        if sub and mag:
            cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (sub[0], mag[0]))
            if not cursor.fetchone():
                cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (sub[0], mag[0], expiration_date))

    # Add entries
    for name in ["Condé Nast", "Meredith", "Hearst"]:
        add_publisher(name)

    add_magazine("Wired", "Condé Nast")
    add_magazine("Vogue", "Condé Nast")
    add_magazine("Better Homes", "Meredith")

    add_subscriber("Alice Smith", "123 Maple St")
    add_subscriber("Bob Jones", "456 Oak Ave")
    add_subscriber("Charlie Brown", "789 Pine Rd")

    add_subscription("Alice Smith", "Wired", "2025-12-31")
    add_subscription("Bob Jones", "Vogue", "2025-11-30")
    add_subscription("Charlie Brown", "Better Homes", "2026-01-15")

    conn.commit()

    # --- Task 4: Run and print SQL queries ---
    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines sorted by name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines from Condé Nast:")
    cursor.execute("""
        SELECT m.name 
        FROM magazines m 
        JOIN publishers p ON m.publisher_id = p.publisher_id 
        WHERE p.name = 'Condé Nast'
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.close()
