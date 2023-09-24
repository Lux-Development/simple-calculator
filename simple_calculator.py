import os 

os.system("title joelb.services")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

function = input("Select operator (+ - * /): ")

final = 0
if function == "+":
    final = num1 + num2

elif function == "-":
    final = num1 - num2

elif function == "*":
    final = num1 * num2

elif function == "/":
    final = num1 / num2

else:
    print("Incorrect operator, please try again.")
    os.system("pause >nul")

print(final)
os.system("pause")