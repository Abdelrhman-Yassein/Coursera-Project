# name =input("Enter Ypur Name ?")
# age = int(input("Enter Your Age"))

# print("Your Name IS " + name )

# if age < 18:
#     raise ValueError("Error:You Need To Be Over 18")
# else:
#     print("your age is " , age)

# number=4
# if number < 5:
#     raise Exception("Error: Value Need To Be Greater Than 5")

# x=1
# y=0
# assert y !=0 ,"invalid operation"

# def print_age(age):
#     assert age > 0,"The value of age muest be  Grearer Than 0"
#     print("your age is ",str(age))
    
# print_age(0)    


# try:
#     num1="4"
#     num2=2
#     result=num1/num2
#     print("end of try block")
# except TypeError:
#     print('TypeError: value has to be an integer')
# else:
#     print("no Exception raised")        
    
try:
    f= open('example.txt',encoding="utf-8")
except FileNotFoundError:
    print("FileNotFoundError : the file not found")   
finally:
    f.close()         