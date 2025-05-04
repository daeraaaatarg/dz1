print("=== Did you get a good score or not? ===")

n = int(input("Enter your result: "))

if 0 <= n <= 49:
    print("Very bad, how can you be that dumb?")
if 50 <= n <= 69:
    print("Still bad, could be better, work harder")
if 70 <= n <= 89:
    print("Very good girl/boy!")
if 90 <= n <= 99:
    print("Well done! Perfect!")
if n == 100:
    print("WONDERCHILD!! ARE YOU GENIUS?!")