class Product:
    def __init__(self, name, basePrice):
        self.__name = name
        self.__basePrice = basePrice
        self.__currentPrice = basePrice
        self.__customers = list()
    def subscribe(self, customer):
        self.__customers.append(customer)
    def unsubscribe(self, customer):
        self.__customers.remove(customer)
    def notify(self):
        for observer in self.__customers:
            observer.update(self)
    def get_name(self):
        return self.__name
    def get_discount(self):
        return (self.__basePrice - self.__currentPrice)*100/self.__basePrice
    def get_currentPrice(self):
        return self.__currentPrice
    def set_currentPrice(self, value):
        self.__currentPrice = value
        if value <= self.__basePrice:
            self.notify()
    name = property(get_name, None, None, None)
    discount = property(get_discount, None, None, None)
    currentPrice = property(get_currentPrice, set_currentPrice, None, None)

class Customer:
    def __init__(self, name):
        self.__name = name
    def update(self, product):
        print("{0}: {1} Laptop is now available at {2}; Discount = {3}%".format(self.__name, product.name, product.currentPrice, product.discount))

Laptop = Product("DELL", 1000)
print("--------Customer 1 and Customer 2 is subscribed to the Laptop Product----------")
Customer1 = Customer("customer 1")
Laptop.subscribe(Customer1)
Customer2 = Customer("customer 2")
Laptop.subscribe(Customer2)
Laptop.currentPrice = 800
print("--------customer 2 is unsubscribed and customer 3 is subscribed to the Laptop Product----------")
Laptop.unsubscribe(Customer2)
Customer3 = Customer("customer 3")
Laptop.subscribe(Customer3)
Laptop.currentPrice = 900