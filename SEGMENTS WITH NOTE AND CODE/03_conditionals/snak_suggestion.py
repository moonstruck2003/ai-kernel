snack = input("Enter your preferred snack: ").lower()

print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa": 
    print("Great choice!! We will serve you {snack}")
else:
    print("Sorry we only serve cookies or samosa with tea!")
