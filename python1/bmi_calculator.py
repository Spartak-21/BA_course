def calculate_bmi(weight, height):
    BMI = weight/(height ** 2)
    return BMI
print("Please enter weigth in kg")
weight = float(input())
print("Please enter heigth in meters")
height = float(input())
BMI = calculate_bmi(weight, height)
if BMI < 18.5: 
    print("Underweight")
elif 18.5 <= BMI < 25: 
    print("Normal weight")
elif 25 <= BMI < 30:
    print("Overweight")
elif BMI >= 30: 
    print("Obese")