import math

# Simple Calculator
a = 8
b = 3

print("Addition : ", a+b)
print("Substraction : ",a-b)
print("Multiplication : ", a*b)
print("Division : ", a/b)



#Area of Shapes
##Area of a Circle
circle_radius = float(input("Enter radius :"))
circle_area = math.pi * circle_radius ** 2
print("Circle Area : ", circle_area)

##Area of a rectangle
rectangle_length= int(input("Enter length :"))
rectangle_width = int(input("Enter width "))
rectangle_area = rectangle_length*rectangle_width
print("Rectangle Area : ", rectangle_area)

##Area of a Triangle
triangle_Base = float(input("Enter Base :"))
triangle_height = float(input("Enter height "))
triangle_area = (triangle_Base*triangle_height)/2
print("triangle area : ", triangle_area)



#Even or Odd
numb = int(input("Enter a number :"))
numberEven = numb % 2
if numberEven == 0:
    print("Even")
else:
    print("Odd")



 #Student Grade percentage
obtained_marks = float(input("Enter your obtained marks : "))
total_marks = float(input("Enter total marks :"))
percent = (obtained_marks/total_marks)*100
print("percentage : ", percent, "%")



#BMI Calculator
Weight = float(input("Enter your Weight (kg) : "))
tall = float(input("Enter your tall (m) : "))
BMI = Weight / (tall**2)
print(" Your BMI is : ", round(BMI, 3))



#Power & Modulus
number1 = 8
exponent_coef = 2
exponent_calcul = number1**exponent_coef
modulus_calcul = number1 % exponent_coef
print(" Your result of exponent : ", exponent_calcul)
print(" Your moulus : ", modulus_calcul )


# What I learned from this exercise is that indentation is very important in Python. We do not declare variables like int number = 8, but rather number = 8. If we want to specify the type, we can write number: int = 8. Finally, exponentiation is done using **.