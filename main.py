import sqlite3,os

class customer:
    def __init__(self, name, email, phone, age, gender, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.gender = gender
        self.address = address

class product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class purchase:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

class database:
    def __init__(self):
        if not os.path.exists("store.db"):
            conn = sqlite3.connect("store.db")
            query = """CREATE TABLE customers(
                customer_id INTEGER PRIMARY KEY,
                customer_name TEXT,
                gender TEXT,
                # dob DATE,
                age INTEGER,
                country TEXT,
                state TEXT,
                city TEXT,
                purchase_date DATE,
                phone_number TEXT,
                email TEXT,
                address TEXT,
                )"""
            query2 = """CREATE TABLE products(
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL,
                category TEXT,
                stock INTEGER,
                quantity INTEGER,
                )"""
            query3 = """CREATE TABLE purchases(
                purchase_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                purchase_date DATE,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
                )"""
            # cursor = sqlite3.cursor()
            conn.execute(query)
            conn.commit()
            conn.close()

    def insert_customer(self, values):
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        query = "INSERT INTO customers (customer_name, gender, age, country, state, city, purchase_date, phone_number, email, address) VALUES (?,?,?,?,?,?,?,?,?,?)" 
        conn.execute(query,values)
        conn.commit()
        conn.close()

    
if __name__=="__main__":
    db = database()

