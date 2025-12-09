class Product:
    count=0 #to count number of objects
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1  

    def get_info(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod  #defining classmethods to find total products
    def get_count(cls):
        print("total product:",cls.count)

    @staticmethod
    def calc_discount(price,percentage):
        total_price= price-(price*percentage/100)
        return total_price

p1=Product("phone",20000)
p2=Product("laptop",30000)
p3=Product("pen",5000)

p1.get_info() #info of product 1
Product.get_count()  #number of products
print(p1.calc_discount(p1.price,20)) #gives total price for product 1