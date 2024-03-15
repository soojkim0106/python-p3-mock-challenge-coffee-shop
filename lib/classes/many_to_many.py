class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise AttributeError(
                "coffee name must be a string with char length of 3 or greater AND attribute already exists"
            )

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        price = [order.price for order in self.orders()]
        return sum(price) / self.num_orders()


class Customer:
    
    all = []
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("customer name must be in string and char between 1 to 15")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(coffee):
        pass
        
        


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee is not instance of Coffee class")
        self._coffee = coffee

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customers is not instance of Customer class")
        self._customer = customer

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not hasattr(self, "_price") and isinstance(price,float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("price must be a float value in between 1.0 and 10.0 and CANNOT be reset")
        
