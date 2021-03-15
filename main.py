# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/height**2)

if bmi < 18.5:
  print(f'Youre bmi is {bmi}, under weight.')
  elif bmi < 25:
    print(f "Youre bmi is {bmi}, you have a normal weight")
  elif bmi < 30:
    print(f'Youre bmi is {bmi},youre slightly obese')
  elif bmi < 35:
    print(f'Youre bmi is {bmi},Youre obese!')
else:
  print(f'Youre bmi is {bmi},Youre clinically obese')



