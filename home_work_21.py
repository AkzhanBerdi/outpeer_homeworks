# phase 1

class Good: # Declaring the Good class
    quantity = 1 # Goods quantity set by default
    def __init__(self, name:str, price:float, quantity:int) -> None: # Initializing Good's class consturctor
        self.name = name # It has a name
        self.price = price # It has a price
        self.quantity = quantity # It has a quantity

    def get_total(self) -> int: # Get total bill method
        return self.price * self.quantity # Total formula is price multiplied by quantity

    def __str__(self) -> str: # Printing total on the screen
         return f"{self.name:<17}{self.price:<7.2f}*  {self.quantity:<3}    = {self.get_total():.2f}" # Returning f-string

# phase 2

class DiscountGood(Good): # Declaring the DicountGood class
    def __init__(self, name:str, price:float, quantity:int, discount:int) -> None: # Initializing DiscountGood's constructor
        super().__init__(name, price, quantity) # Inheriting Good's attributes
        self.discount = discount # It has the discount attribute beside inherited Good's attributes 

    def get_total(self) -> int: # #Get total bill taking into account new attribute
        return super().get_total()-self.price/100*self.discount # Inherited get_total method plus discount calculation
    
    def __str__(self) -> str: # Printing total on the screen 
        return super().__str__() + f'-({self.discount}%)' # Inheriting __str__ method from Goods with discount displayed

# phase 3

class Cart(Good): # Declaring the Cart class
    
    def __init__(self,goods:list[Good,DiscountGood]) -> None: # Initializing Cart's constructor
        self.goods = goods # It has list of Goods and or DiscountGoods
        
    def get_cart_total(self) -> int: # Get entire list total taking into account discount
        total = 0 # Returning variable for total cart pricem which equals zero for a while being
        for good in self.goods: # Looping through a list of objects
            if isinstance(good, DiscountGood) and good.discount > 0: # Checking if the good is an instance of DiscountGood and it has a proper discount value
                total += good.price * good.quantity - good.price / 100 * good.discount # In case of DicountGood instance the total variable gets addition which is taking into account discount variable
            else: # We assume that the rest of the instance are Good instances
                total += good.price * good.quantity # In case of which the total gets addition by simple price*quantity multiplication
        return total # Returning the variable as the calculated cart total
       

    def __str__(self) -> str: # We breaking down this method into 3 main parts: Header, Body and Footer   
        header = f"{'Name':<25}{'PPU':<7}{'CNT':<7}{'Price':<7}{'DISC':<8}\n{'='*70}\n"  # Initializing the Header
        body = '' # Initializing the Body
        
        for good in self.goods: # Iterate through the goods list and add each item to the body
            if isinstance(good, DiscountGood): # If the item is a DiscountGood, calculate the discounted price
                price = (good.price * good.quantity) * (1 - good.discount / 100) # Discount formula applied
                discount_str = f"(-{good.discount}%)"  # Generating the discount string for instances of DiscountGood
            else:
                price = good.price * good.quantity # If the item is instance of Good, simply calculate the price
                discount_str = '' # There's no discount, so the discount string is empty
                
            item_str = f"{good.name:<25}{good.price:<7.2f}* {good.quantity:<7} {price:<7.2f}{discount_str}\n" # Generating the formatted string for each good.item
            body += item_str # Add the formatted string to the Body

        total = self.get_cart_total() # Calculate the total price of the cart

        footer = f"{'='*70}\n{'Total':<41} = {total}\n" # Generate the footer string
  
        return header + body + footer # Combine the header, goods, and footer strings and return the result

goods = [
        Good('Bread', 17, 3),
        Good('Water', 19, 2),
        DiscountGood('Juice', 80, 1, 20),
        Good('Toilet Paper', 19, 10)
] # List of Goods as per home work requirements

cart = Cart(goods)  # Creating the object of Cart

print(cart.__str__()) # Printing out the total