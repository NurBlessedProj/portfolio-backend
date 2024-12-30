import calcul

a = int(input("Please enter the first number :"))
b = int(input("Please enter the second number :"))
sign = input("Please select one sign in +, - , * , / :")

result = None

if sign == "+":
    result = calcul.addition(a, b)
elif sign == "-":
    result = calcul.subtraction(a, b)
elif sign == "*":
    result = calcul.multiplication(a, b)
elif sign == "/":
    result = calcul.division(a, b)
else:
    result = "invalid method"

print(f"Result : {result}")
