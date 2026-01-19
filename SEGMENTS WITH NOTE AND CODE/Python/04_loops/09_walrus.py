# value = 13

# remainder = value % 5

# if remainder: 
#     print(f"Not divisible, remainder is {remainder}")


# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")



# avail = ["small","big","med"]

# if (req_size := input("enter your chai cup size: ")) in avail: 
#     print("Serving {req_size} - ")

# else:
#     print("not availble")


flavors = ["masala","ginger","lemon"]

print("available fablours : {flavors}")

while(flavors := input("choose your flavor: ")) not in flavors: 
    print(f"sorry {flavors} not avialbe")


print(f"aviable")