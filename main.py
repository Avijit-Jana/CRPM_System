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


if __name__=="__main__":
    c = customer()
    p = product()
    pur = purchase()
