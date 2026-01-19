chai = input("Choose your cup size: ").lower()

if chai == "small":
    print(f"Your price is 10 tk")
elif chai == "medium":
    print(f"Price is 15 rupees")
elif chai == "large":
    print(f"Price is 20 tk")

else:
    print("Unknown cup siize")