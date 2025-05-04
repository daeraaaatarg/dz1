print("=== GENIUS CALCULATOR IN PYTHON *cheering,clapping* ===")

a = float(input("Enter your number 1: "))
b = float(input("Enter your number 2: "))
sign = input("Enter you sign(+,-,*,/): ")

if sign == "+":
    suma = a + b
    print(f"Suma is {suma}")
if sign == "-":
    diff = a - b
    print(f"Difference is {diff}")
if sign == "*":
    multi = a * b
    print(f"Product is {multi}")
if sign == "/":
    if b == 0:
        print("Fool, you cannot divide by zero")
    if b != 0:
        div = a / b
        print(f"Fraction is {div}")