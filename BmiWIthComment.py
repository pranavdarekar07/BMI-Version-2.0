print("BMI Calulator\n ************************************ \n Condition :- \n Underweight = <18.5 \n Normal weight = 18.5–24.9 \n Overweight = 25–29.9 \n Obesity = BMI of 30 or greater \n ************************************")
height = int(input("Your Height : "))
weight = int(input("Your Weight : "))
BMI = round((weight / height ** 2)*10000,2)
print(BMI)
if BMI <= 18.5:
    print("Sorry to say but, you are Underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are absolutely fine.")
elif 25 <= BMI <= 29.9:
    print("Your are Overweight. Do some diet to get fit and fine.")
elif 30 <= BMI:
    print("You are obesity. Please contact doctor.")
else:
    print("Error")