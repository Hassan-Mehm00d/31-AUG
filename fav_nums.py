
# gathering all the data required
fav_list : list = []
name: str = input("Enter your name pal: ")
fav_list.append(int(input("Enter your first favorite number: ")))
fav_list.append(int(input("Enter your second favorite number: ")))
fav_list.append(int(input("Enter your third favorite number: ")))

# greeting the user
print(f"Hello, {name.title()} lets explore your favorite numbers:")

# checking numbers whether odd or even
for number in fav_list:
    if number % 2 == 0:
        print(f"The number {number} is even. ")
    else:
        print(f"The number {number} is odd.")

# printing their squares and sum
    square = number * number
    print(f"The number {number} and its square: ({number}, {square})")


total = sum(fav_list)
print(f"Amazing! The sum of your favorite numbers is {total}")

# checking whether total is prime or not
if total > 1:
    prime = True
    for check in range(2, int(total ** 0.5) + 1):
        if total % check == 0:
            prime = False
            break
    if prime:
        print(f'{total} is a prime number.')
    else:
        print(f"{total} is a composite number.")
else:
    print(f"{total} is not a prime number (by definition)")