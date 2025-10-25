#Basic task
#1
num = int(input("Enter number :"))
if (num % 2) == 0 :
    print("Its even")
else:
    print("its odd")

#2
num = int(input("Enter number :"))
if (num > 0):
    print("positive")
else:
    print("Its Nagitive")

#
password = "mujha_nahi_pata"
user = input("Enter password :")
if password == user :
    print("Access granted")
else:
    print('Access denied')

#Mrdium level
#1
num1 = int(input("Enter first numder :"))
num2 = int(input("Enter 2nd number : "))
optr = input("Enter operator :")
if optr == "+":
    print(num1+num2)
elif optr == "-":
    print("num1-num2")
elif optr =="*":
    print(num1*num2)
else:
    print(num1/num2)

#2
age = int(input("Enter your age :"))
if age <= 13:
    print("You are childern")
elif age > 13 and age <= 19:
    print("Enjoy! its your teen age")
elif age >19 and age <= 59:
    print("You are adult")
else:
    print("Allah allah karan sir")


#3
secret = "wajid"
user_try =""
while secret != user_try:
    user_try = input("Wrong! try again")
    print("You won")
    
#Bit tough
#1


secret = "123456"
att = ""
att_count = 0
t_att = 3
out_of_att = False
while att != secret and not(out_of_att):
    if att_count<t_att:
        att =input("Wrong! try again :")
        att_count+=1
    else:
        out_of_att = True
if out_of_att:
    print("You lose")
else:
    ("You won")

#2
num = int(input("Enter number:"))
i =1
while i<=10:
    print(num*i)
    i += 1


#2

password = input("Creat password :")
length = len(password)>= 8
uppercase = any(char.isupper() for char in password)
has_num= any(char.isdigit() for char in password)
if length and uppercase and has_num:
    print("Strong password")
else:
    print("Week password")




