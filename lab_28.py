from fractions import Fraction

class BaseMoney:
    def __init__(self, wholes:int, cents:int) -> None:
        self.wholes = wholes
        self.cents = cents
        self.validate(cents)

    def validate(self, cents:int) -> None:
        if cents > 99:
            x = self.cents // 100
            self.wholes += x
            self.cents = cents - x * 100
        elif cents < 0:
            raise ValueError("Try absolute values")

    def __str__(self):
        return f"{self.wholes}.{self.cents}"

    def __add__(self,other:'BaseMoney') -> 'BaseMoney':
        sum_wholes = self.wholes + other.wholes
        sum_cents = self.cents + other.cents
        if sum_cents > 99:
            x = sum_cents // 100
            sum_wholes += x
            sum_cents -= x * 100
        return BaseMoney(sum_wholes, sum_cents)

    def __sub__(self, other:'BaseMoney') -> 'BaseMoney':
        sum_wholes = self.wholes - other.wholes
        sum_cents = self.cents - other.cents            
        if self.wholes < other.wholes:
            raise ValueError("A should be bigger than B")
        if self.cents < other.cents:
            sum_wholes -= 1
            sum_cents += 100
        return BaseMoney(sum_wholes,sum_cents)

    def divide(self,other:'BaseMoney') -> 'BaseMoney':
        x = self.wholes * 100 + self.cents
        y = other.wholes * 100 + other.cents
        return Fraction(x,y)

    def numMultiply(self,num:int) -> 'BaseMoney':
        sum_wholes = self.wholes * num 
        sum_cents = self.cents * num
        sum_wholes += sum_cents // 100
        if sum_cents > 99:
            sum_cents = sum_cents % 100
        return BaseMoney(sum_wholes,sum_cents)
    
    def numDivision(self,num:int) -> 'BaseMoney':
        total_cents = self.wholes * 100 + self.cents
        total_cents /= num
        return BaseMoney(int(total_cents//100),int(total_cents%100))

    def moneyComparison(self,other:'BaseMoney') -> 'BaseMoney':
        if self.wholes > other.wholes:
            return f"A is bigger than B"
        elif self.wholes == other.wholes:
            if self.cents > other.cents:
                return f"A is bigger than B"
            elif self.cents == other.cents:
                return f"A is equal to B"
            else:
                return f"A is less than B"
        else:
            return f"A is less than B"


a = BaseMoney(100,00)
b = BaseMoney(100,00)
# print(a.__add__(b))
# print(BaseMoney.__sub__(a,b))
# print(a.numMultiply(100))
# print(BaseMoney.numDivision(a,100))
# print(a.moneyComparison(b))
# print(BaseMoney.divide(a,b))

class Money(BaseMoney):

    CURRENCIES = {'KGS': 4, 'USD': 450, 'RUR': 5, 'EUR': 500, 'KZT': 1}

    def __init__(self, wholes: int, cents: int, currency: str) -> None:
        super().__init__(wholes, cents)
        self.currency = currency
        if currency not in Money.CURRENCIES:
            raise ValueError("Unknown currency")
        
    def convert(self, other: str) -> 'Money':
        value = self.wholes + self.cents /100
        kzt_value = value * Money.CURRENCIES[self.currency]
        new_value = kzt_value / Money.CURRENCIES[other]
        return '%.2f' % new_value

c = Money(100,00,'EUR')
print(Money.convert(c,'USD'))

