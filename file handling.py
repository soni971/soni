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
    
# remove=1
# with open("abc.txt","r")as f:
#     lines=f.readlines()
# with open("abc.txt","w")as f:
#     for i ,line in enumerate(lines):
#         if i!= remove:
#             f.write(line)



# #CREATE A FLODER
# import os
# os.mkdir("soni")


# # RENAME 
# os.rename("soni","ram")

# RENAME OF FILEWS
# os.rmdir("ram")

# import shutil
# shutil.rmtree("AIPA")


#LIST ALL FILES IN FLODER
# xyz=os.listdir(".")
# print(xyz)
# xyz=os.listdir()
# print(xyz)


# abc=os.getcwd()
# print(abc)



# # CWD CURRENT WORKING DIRECTORY
# import os
# os.mkdir("AIPA")
# with open("AIPA/student.txt", "w") as file:
#     file.write("""student details: jiya,riya,priya""")
# print("details add")    

# import os
# os.mkdir("Animal")
# with open("Animal/pet name.txt","w") as files:
#     files.write("""pet name :
# 1. MAX
# 2. BELLA
# 3. ROCKY""")
# print("details add")   


import os 
# os.mkdir("student Data")
# os.mkdir("student Data/Assignments")
# os.rename("student Data/Assignments ","student Data/Submissions")
with open("student Data/Submissions/info.txt","w")as file:
    file.write("This is initial content.")
with open("student Data/Submissions/info.txt","a")as file:
    file.write("/nThis is the appended content.")
