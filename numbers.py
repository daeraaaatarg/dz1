print("=== Numbers in your diapason ===")

start = int(input("Start of the diapason: "))
end = int(input("End of the diapason: "))

print(f"Numbers from {start} to {end}: ")
if start <= end:
        for i in range(start, end + 1):
            print(i, end=" ")
else:
        for i in range(start, end - 1, -1):
            print(i, end=" ")

print(" ")

print("=== Even numbers from 1 to n in reverse order ===")

n = int(input("Enter the n: "))

print(f"Even numbers from 1 to {n} in reverse order:")
for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")