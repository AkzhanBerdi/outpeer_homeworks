
class User:
    def __init__(self,f_name, l_name, passport) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.__passport = passport

    def get_passport(self):
        return self.__passport
    
    def set_passport(self, passport_number):
        if len(str(passport_number)) < 12 > 0:
            self.__passport = passport_number
            return self.__passport
        else:
            print('ivalid passport number')


    def take_payment(self):
        print('Transaction Complete')

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'
    
        
        
class Employee(User):
    def __init__(self,f_name, l_name, passport) -> None:
        super().__init__(self.f_name, self.l_name, self.passport)
        self.passport = passport
        print('class Employee')

    def __str__(self) -> str:
        return super().__str__() + f"self.passport"
    
user1 = User('Akzhan','Berdi',45678)
user1.set_passport(987654345)
print(user1)

"""
class Customer(User):
    pass

class Cashier(Employee):
    def __init__(self,f_name, l_name,passport) -> None:
        super().__init__(f_name,l_name,passport)
        print('class Cashier')

#john = Employee('John', 'Snow', 88765789)
bryan = Cashier('Bryan', 'Brown', 4123451)
print(bryan)"""