# #  OOPS CONCEPT
# class student:
#        def __init__(self,name,trade):
#         self.name=name
#         self.trade=trade
# s1=student("Soni","AIPA")
# s2=student("Jiya","CSA")
# s3=student("Shivali","COPA")
# print(s1.name,s1.trade) 
# print(s2.name,s2.trade)
# print(s3.name,s3.trade)


# class Person:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
# s1=Person("Soni","A")
# s2=Person("Jiya","B")
# s3=Person("Riya","A")
# print(s1.name,s1.grade)
# print(s2.name,s2.grade)
# print(s3.name,s3.grade)  



# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

         
        

# BANK ACCOUNT
class BankAccount:

    def __init__(self,balance):
        self.balance=balance
    def add(self,amt):
            self.balance+=amt
    def withdraw(self,amt):
                self.balance -=amt
    def finalamount(self):
            return self.balance
initial=int(input("Enter the Amount"))
deposit=int(input("Enter the deposit"))
acc=BankAccount(initial)
acc.add(deposit)
acc.withdraw(500)
print(acc.finalamount())


class bankaccount:
       def __init__(self,balance):
              self.balance=balance
       def add(self,amt):
              self.balance+=amt 
       def withdraw(self,amt):
                self.balance -=amt
       def finalamount(self):
            return self.balance
acc=bankaccount(2000)       
acc.add(500)
acc.withdraw(100)
print(acc.finalamount())    
            


        
