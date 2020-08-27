# BMI Calculator
# created by AusbildungmitZukunft
import locale
locale.setlocale(locale.LC_ALL,'de_DE')
print("\tBMI Calculator")
height = input("Please input your height in meters\n")
height1 = locale.atof(height)
weight = int(input("Please input your weight\n"))
bmi = (weight/(height1*height1))

if bmi <= 18:
      print("Your BMI is ", bmi,"you are underweight.")
elif 18 > bmi < 25:
      print("Your BMI is ", bmi,"You are normal weight.")
elif 25 > bmi < 30:
      print("Your BMI is ", bmi,"You are overweight.")
elif bmi > 30:
      print("Your BMI is", bmi,"You are obese.")

else:
    print("An error occurred when you entered your parameters")
    print("Please check whether you entered an integer\n")