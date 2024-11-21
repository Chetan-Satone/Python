"""Problem Statement 2: Inventory Management System*
Design a Python program to manage product inventory in a store.  
1. Create a class Product with attributes:
   - product_name (string): Name of the product.  
   - product_id (integer): Unique ID for the product.  
   - price (float): Price of the product per unit.  
   - stock (integer): Quantity of the product in stock.  

2. Add a method sell_product(quantity):
   - If quantity is available in stock, reduce the stock by the specified quantity and return the total price.  
   - If quantity is not available, return "Insufficient stock."

*Example*:  
Input: Product("Laptop", 202, 55000, 10)  
Selling 3 units: sell_product(3) -> Output: ₹165000, Remaining Stock: 7  
Selling 15 units: sell_product(15) -> Output: "Insufficient stock"""


class Product:
    def init(self):
        self.name= str(input("Enter the name of the product "))
        self.id = int(input("id of the product"))
        self.price =float(input("price of the product "))
        self.stock= int(input("quantity "))

    def sell_product(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            total_price = self.price * quantity
            return f"₹{total_price}, Remaining Stock: {self.stock}"
        else:
            return "Insufficient stock."
        
a1=Product()
a1.init()
print(a1.sell_product(5))
print(a1.sell_product(1))



