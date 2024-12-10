import sqlite3, os

class Database:
    def __init__(self, db):
        self.db = db
        if not os.path.exists(db):
            self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db)
        conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
        cursor = conn.cursor()

        # Create the `customers` table
        query_customers = """
        CREATE TABLE IF NOT EXISTS customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT, 
            gender TEXT,
            age INTEGER, 
            country TEXT, 
            state TEXT, 
            city TEXT, 
            order_date TEXT, 
            phone TEXT, 
            email TEXT, 
            order_status TEXT, 
            product_name TEXT, 
            quantity INTEGER, 
            address TEXT
        )
        """        

        # Create the `products` table
        query_products = """
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT, 
            stock INTEGER, 
            color TEXT, 
            category TEXT,
            cost_price REAL, 
            discount REAL, 
            brand TEXT, 
            unit_price REAL, 
            product_status TEXT, 
            product_description TEXT
        )
        """

        # Create the `purchases` table
        query_purchases = """CREATE TABLE IF NOT EXISTS purchases(
            purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,                
            customer_name TEXT,
            phone TEXT,
            product_id INTEGER,
            product_name TEXT,
            brand TEXT,
            quantity INTEGER,
            unit_price REAL,
            Toatal Price REAL = quantity * unit_price,
            purchase_date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (customer_name) REFERENCES customers(customer_name),
            FOREIGN KEY (phone) REFERENCES customers(phone),
            FOREIGN KEY (product_name) REFERENCES products(product_name),
            FOREIGN KEY (brand) REFERENCES products(brand),
            FOREIGN KEY (quantity) REFERENCES customers(quantity),
            FOREIGN KEY (purchase_date) REFERENCES customers(order_date),
            FOREIGN KEY (unit_price) REFERENCES products(unit_price))"""

        # Execute table creation queries
        cursor.execute(query_customers)
        cursor.execute(query_products)
        cursor.execute(query_purchases)
        conn.commit()
        conn.close()

    def add_customer(self, values):
        try:
            conn = sqlite3.connect(self.db)
            conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
            cursor = conn.cursor()
            query = """INSERT INTO customers 
            (customer_name, gender, age, country, state, city, order_date, phone, email, order_status, product_name, quantity, address) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""        
            cursor.execute(query, values)
            conn.commit()
            return "Customer data inserted successfully."
        except sqlite3.Error as e:
            return f"An error occurred while inserting customer data: {e}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    # def update_customer(customer_id, name, email, phone):
    #     conn = sqlite3.connect("store.db")
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #         UPDATE customers
    #         SET name = ?, email = ?, phone = ?
    #         WHERE customer_id = ?
    #     """, (name, email, phone, customer_id))
    #     conn.commit()
    #     conn.close()

    # def deactivate_customer(customer_id):
    #     conn = sqlite3.connect("store.db")
    #     cursor = conn.cursor()
    #     cursor.execute("UPDATE customers SET status = 'inactive' WHERE customer_id = ?", (customer_id,))
    #     conn.commit()
    #     conn.close()

    # def view_customers():
    #     conn = sqlite3.connect("store.db")
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM customers WHERE status = 'active'")
    #     customers = cursor.fetchall()
    #     conn.close()
    #     return customers

    def add_product(self, values):
        try:
            conn = sqlite3.connect("store.db")
            conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
            cursor = conn.cursor()
            query = """
            INSERT INTO products 
            (product_name, stock, color, category, cost_price, discount, brand, unit_price, product_status, product_description) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, values)
            conn.commit()
            return "Product data inserted successfully."
        except sqlite3.Error as e:
            return f"An error occurred while inserting product data: {e}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()
