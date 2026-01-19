#BOOLEAN 

is_boiling = True
stir_count = 5

total_actions = stir_count + is_boiling  #True is treated as 1 in arithmetic operations, upcasting 

print("Total Actions :", total_actions)


milk_present = 0 #Milk is absent ,0 , none 

print(f"Is three milk present? : {bool(milk_present)}")  #0 is treated as False in boolean context  


water_hot = True 

tea_added = False 

can_serve_tea = water_hot and tea_added  #Logical AND operation

print(f"Can we serve tea? : {can_serve_tea}")


