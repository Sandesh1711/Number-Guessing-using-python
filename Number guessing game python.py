import random

num = random.randrange(1,101)

user_input = int(input("Enter your number:-"))
print(num)
if user_input == num:
    print("Your gussing is matched.")

elif user_input > num:
    print("Your guess is too high.")

else:
    print("your guessing is too low. ")