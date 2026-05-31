#Age Eligibility Checker
age = int(input("Enter your age : "))

if age < 13 :
    print("You are a child!")
elif age <20:
    print("You are a teenager!")
else:
    print("You are a adult!")



#Password validator
Password_validator = input(" Enter your password : ")
if len(Password_validator)>=8:
    print(" Your password is strong, good!")
else:
    print("Your password is weak, improve it a 8 character!")




#Grade Classification
score = int(input("Enter Your score : "))

if score >=18:
    print("Your grade is A")
elif score<18 and score>=15:
    print("Your grade is B")
elif score<15 and score>=12:
    print("Your grade is C")
else:
    print("Your grade is D") 



#Multiplication Table
number = int(input("Enter a number : "))

for i in range(1,13):
    print(f"{number} * {i}= ({number}*{i})")



#Number guessing Game
guess_number = 10
guess = 0

while guess!=guess_number:
    guess = int(input("Guess the number :"))
if guess ==guess_number:
    print("Correct number !")
else:
    print("Try agin")



#Countdown Timer
for j in range(11, 0, 1):
    print(j)
print("Time'S UP!")



#ATM Withdrawal simulation
balance = 100000

Withdrawal = float(input("Enter amount to withdraw : "))
if Withdrawal<=balance:
    balance-=Withdrawal
    print("withdrawal Successful")
    print("Remaning balance :", balance)
else:
    print("Remaining funds")



#Login system
username = "Dany"
password = "DanilovePython3"

username_enter = input("Enter  your username :")
password_enter = input("Enter your password")

if username_enter==username and password_enter==password:
    print("Login successfull")
else:
    print("invalid informations")