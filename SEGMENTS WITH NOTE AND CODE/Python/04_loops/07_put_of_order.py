flav = ["ginger","out of stock","lemon","discontinued","tulsi"]

for fla in flav: 
    if fla == "out of stock":
        continue
    if fla == "discontinued":
        break
    print("{fla} item found ")
    
print("Discontinued item found out of loop ")
      
