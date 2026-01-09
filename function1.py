# def add(a,b):
#     return a+b
# print(add(54,96))


# def sub(a,b,c):
#     return(a-b-c)
# print(sub(66,41,12))

# def seq(a):
#     return 8**2
# print(seq(8))



# READ,WRITE,APPEND


# x=open("abc.txt","r")
# y=x.read()
# print(y)
# x.close()

# x=open("abc.txt","w")
# x.write("This is new contract\n")
# x.write("Welcome to new code")

# M=open("abc.txt","a")
# M.write("\nLove Animal\n")
# M.write("Dogs")


# with open("abc.txt","r")as file:
#      print(file.read())
# file=open("abc.txt","r")
# # file.close()    
# with open("notes.txt","a")as f:
#   f.write("Shinchan\n")
#   f.write("I Love India,\n")
#   print("Data appeneded successfully!")



# with open("abc.txt","r")as file:
#      lines=file.readlines()
#      word="Welcome to new code"
#      with open("abc.txt","w")as file:
#           for line in lines:
#                if word not in line:
#                 file.write(line)
    
remove=1
with open("abc.txt","r")as f:
    lines=f.readlines()
with open("abc.txt","w")as f:
    for i ,line in enumerate(lines):
        if i!= remove:
            f.write(line)
        
        
