import sqlite3, os

class Database:
    def __init__(self):
        if not os.path.exists("store.db"):
            self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect("store.db")
        conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
        cursor = conn.cursor()

        query_customers = """CREATE TABLE IF NOT EXISTS customers(
            customer_name TEXT,
            gender TEXT,
            age INTEGER,
            country TEXT,
            state TEXT,
            city TEXT,
            email TEXT,
            phone_number TEXT PRIMARY KEY,   
            purchase_date DATE,  
            address TEXT
        )"""        

        query_products = """CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            stock INTEGER,
            quantity INTEGER,
            order_date TEXT,
            price REAL,
            status TEXT,
            category TEXT,
            product_description TEXT
        )"""

        query_purchases = """CREATE TABLE IF NOT EXISTS purchases(
            purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            purchase_date TEXT,
            FOREIGN KEY (phone_number) REFERENCES customers(phone_number),
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (purchase_date) REFERENCES customers(purchase_date),
        )"""

        cursor.execute(query_customers)
        cursor.execute(query_products)
        cursor.execute(query_purchases)
        conn.commit()
        conn.close()

    def insert_customer(self, values):
        try:
            conn = sqlite3.connect("store.db")
            conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
            cursor = conn.cursor()
            query = """INSERT INTO customers 
            (customer_name, gender, age, country, state, city, purchase_date, phone_number, email, address)
            VALUES (?,?,?,?,?,?,?,?,?,?)"""
            cursor.execute(query, values)
            conn.commit()
            return "Customer data inserted successfully."
        except sqlite3.Error as e:
            return f"An error occurred while inserting customer data: {e}"
        finally:
            conn.close()

    def insert_product(self, values):
        try:
            conn = sqlite3.connect("store.db")
            conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
            cursor = conn.cursor()
            query = """INSERT INTO products 
            (product_name, quantity, order_date, price, status, category, stock, product_description)
            VALUES (?,?,?,?,?,?,?,?)"""
            cursor.execute(query, values)
            conn.commit()
            return "Product data inserted successfully."
        except sqlite3.Error as e:
            return f"An error occurred while inserting product data: {e}"
        finally:
            conn.close()
