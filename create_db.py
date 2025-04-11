# create_db.py
import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Drop table if it already exists (to avoid duplicate entries)
c.execute("DROP TABLE IF EXISTS products")

# Create the table
c.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price REAL
    )
''')

# Product data (in Rupees ₹)
products = [
    ("Laptop", "Gaming laptop with RTX graphics", 95000),
    ("Phone", "Android smartphone with AMOLED display", 25000),
    ("Headphones", "Noise cancelling over-ear headphones", 5500),
    ("Mouse", "Wireless mouse with ergonomic design", 1200),
    ("Keyboard", "Mechanical keyboard with RGB lighting", 3000),
    ("Monitor", "27-inch Full HD monitor", 12000),
    ("Power Bank", "10000mAh fast-charging power bank", 1500),
    ("Charger", "Fast charging USB-C charger", 800),
    ("Smartwatch", "Fitness smartwatch with heart monitor", 4500),
    ("Tablet", "10-inch Android tablet", 18000),
    ("Speaker", "Bluetooth speaker with bass boost", 2300),
    ("Webcam", "1080p HD USB webcam", 2000),
    ("Printer", "All-in-one inkjet printer", 7000),
    ("Desk Lamp", "LED desk lamp with brightness control", 1000),
    ("USB Drive", "64GB USB 3.0 pen drive", 600)
]

# Insert data
c.executemany("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", products)

conn.commit()
conn.close()
