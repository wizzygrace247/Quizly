class Discount:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def viewDetails(self):
     print(f"{self.name} {self.color} {self.price}")

car1 = Discount("dodge","red", 50000).viewDetails()

class child(Discount):
   pass
car2 = child("porsh","red", 50000).viewDetails() 