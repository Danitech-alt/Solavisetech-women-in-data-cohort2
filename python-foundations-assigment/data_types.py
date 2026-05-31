#My Personal Bio Generator
name = "Danielle Mabouanda"
age = 24
height = 1.60
favorite_tech_field = "Full stack developer"
is_student = False

print(
    f"My name is {name}, I am {age} years old, "
    f"{height} m tall, interested in {favorite_tech_field}, "
    f"and student tatus is {is_student}."
)



#Type Checker
num = 24
price = 5.84
text = "python"
status = True

print(type(num))
print(type(price))
print(type(text))
print(type(status))



#Data Conversion
##Integer to string
integer_number = 2002
string_number = str(integer_number)
print(string_number)

##float to integer
float_number = 1.60
integer_number_1 = int(float_number)
print(integer_number_1)

##string to integer
string_number = "16_01_2026"
integer_number_2 = int(string_number)
print(integer_number_2)



#User Information
user_name = input("Enter your name : ")
user_age = input("Enter your age :")
user_country = input("Enter your country :")

print(
    f"hello my dear {user_name} I'm glad to meet you, "
    f"you have {user_age} years old "
    f"and you live in {user_country}."
)



#Temperarture Converter
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature is {celsius} C = {fahrenheit} F")

