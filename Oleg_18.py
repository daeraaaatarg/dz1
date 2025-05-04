name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Meeting: Hello, I'm {name} and I am {age} years old")
if age >= 18:
    print("Enter allowed")
if age < 18:
    print("Go away, little puppy")