staff = [("amith",16),("Zara",12),("raz",15)]

for name,age in staff: 
    if age<=18:
        print(f"{name} is eligible to manage the stuff")
        break
else:
    print(f"No one is eliblible to manage the stuff") # else block only runs when nothing in te for loop runs