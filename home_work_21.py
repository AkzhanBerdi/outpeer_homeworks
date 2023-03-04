# phase 1

class Good:
    quantity = 1
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quanity = quantity

    def get_total(self, price, quantity):
        self.total = price * quantity
    
    def __str__(self) -> str:
        return f'{self.name:20} {self.price:<7.2f} * {self.quanity:3} = {self.get_total:10.2f}'
    
# phase 2

class DiscountGood(Good):
    def __init__(self, name, price, quantity, discount) -> None:
        super().__init__(name, price, quantity)
        self.discount = discount

    def get_total(self, price, quantity,discount):
        return super().get_total(price, quantity)/discount
    
    def __str__(self) -> str:
        return super().__str__()


#    def get_total_after_discount(self,price,quantity,discount):
 #       self.total_after_discount = price * quantity / discount

# phase 3
class Cart:

    def get_total(self, price, quantity):
        return super().get_total(price, quantity)
    
    def __str__(self) -> str:
        return super().__str__()
    

Bread = Good('Bread', 17,3)
Water = Good('Water', 19,2)
Juice = DiscountGood('Juice',80,1,20)
Toilet_Paper = Good('Toilet Paper', 19,10)
goods = [Bread,Water,Juice,Toilet_Paper]

cart= Cart(goods)

print(Bread.get_total())