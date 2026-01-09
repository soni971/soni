# # # # PRACTICE QUESTION

# # # # QUESTION 1:
# import math
# r=pow(3,6)
# print(math.pi*r)


# # # # QUESTION 2:

# import math

# print(math.factorial(int(input("enter factorial num:"))))
# print(math.sqrt(int(input("enter square num:"))))


# # # # QUESTION 3:

# import random
# print("and the num is:",random.choice([1,50]))


# # # #QUESTION 5:

# import datetime
# today=datetime.date.today()
# print("today date:",today)
# print("day name:",today. day)
# print("year:",today.year)

# import time
# print(time.ctime())



# #QUESTION 6:
# #DATE THAT WAS 10 DAYS AGO AND 10 DAYS LATER

# import datetime
# today=datetime.date.today()
# past=today-datetime.timedelta(days=10)
# future=today+datetime.timedelta(days=10)
# print("10 days ago:",past)
# print("10 days later:",future)


# # QUESTION 7:
# # PRINT CURRENT WORKING DIRECTORY

# import os
# print("current working directory:",os.getcwd)


# QUESTION 8:
# LIST ALL FILES AND FLODER IN CURRENT DIRECTORY



# # # QUESTION 9:

# import sys
# print(sys.version)
# print(sys.platform)



# # # QUESTION 10 :
# # import platform
# print("Operating System:",platform.system())
# print("Python Version:",platform.python_version()) 



# EXCEPTIONAL HANDLING
# try:
#    a=5
#    b=int(input("enter your number"))
#    print(a/b)
# except ZeroDivisionError:
#    print("Number cant't be divided by 0")
# X=10
# Y=12
# print(X-Y)


# try:
#     a=9
#     x=int(input("enter your number"))
#     print(10/x)
# except ZeroDivisionError:
#     print("cant't divided by 0")
# except ValueError:
#     print("cant't divided by string")        
# else:
#     print("the input number was:",x)
# finally:
#     print("All code done:")




# # INDEX ERROR
# x=["A","B","C","D","E"]
# print(x[9])



# # SYNTAX ERROR
# if 6>3
#     print("six is greater")

# # NAME ERRPR
# trade="AIPA"
# print(trede)


# # LOGICALLY ERROR
# a=(1,2,3,4,5,6,7,8,9,)
# b=sum(a)/len(1)
# print(b)


# class nstiadmisson (Exception):
#     pass
# try:
#     x=(input("enter age:"))
#     if x<=20:
#         raise nstiadmisson ("not age")
#     else:
#         print(" you are eligible")
# except nstiadmisson as on:
#     print("reason:",on)

# class AadharCard(Exception):
#     pass
# try:
#     aadhar=(input("Enter your Aadhar number"))
#     if len(aadhar)!=12:
#         raise AadharCard("Invaild Aadhar number")
#     else:
#         print("Aadhar number is verified successfully!")
# except AadharCard as Shinchan:
#     print("Reason:",Shinchan)


# # class Bussiness(Exception):
# #     pass
# # try:
# #     investement=(input("Enter your investment amount"))
# #     if investement<50000:
# #         raise Bussiness("You are not eligible-minimum 50000 required for registration.")
# #     else:
# #         print("You are eligible to start the Bussiness")
# # except Bussiness as Holder:
# #     print("Reason:",Holder)         


# def main():
#   try:
#     print("1.Addition")
#     print("2.Substration")
#     print("3 Multiple")
#     print("4 Division")
#     choice=int(input("enter you choice(1/2/3/4/):"))
#     x=int(input("Enter you choice 1:"))
#     y=int(input("Enter number 2:"))
#     if choice==1:
#       result=x+y
#       print(result)
#     elif choice==2:
#       result=x-y
#       print(result)
#     elif choice==3:
#       result=x*y
#       print(result)
#     elif choice==4:
#       if y!=0:
#         return x/y
#     else:
#       print("can't divide")
#   except ZeroDivisionError:
#     print("can't divide by 0")
#   except ValueError:
#     print("Enter valid number:")
#   else:
#     print("Number are:",x,y)
#   finally:
#     print("Calculate created!")
# if __name__=="__main__":
#   main()


import os
os.mkdir("abc.txt.py")