print("Your numbers are:")
x = float(input("First number = "))
y = float(input("Second number = "))

print("Select operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
choice = input("1/2/3/4 - ")

if choice == "1":
    print(x+y)
elif choice == "2":
    print(x-y)
elif choice == "3":
    print(x*y)
elif choice == "4":
    print(x/y)
else:
    print("Incorrect data")

print("Thanks for attention")