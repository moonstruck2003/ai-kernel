ingredients = ["water", "milk", "sugar"]

ingredients.append("tea leaves")  #Modifying the list by adding an element as Mutable

print(f"Ingredients List: {ingredients}")

ingredients.remove("sugar")  #Modifying the list by removing an element as Mutable	
print(f"Ingredients List after removing sugar: {ingredients}")

spice_options = ["cardamom", "cinnamon"]	
chai_ingredients = ["water", "milk"] 

chai_ingredients.extend(spice_options)  #Combining two lists using extend method

print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "sugar")  #Inserting an element at specific index
print(f"chai: {chai_ingredients}")


last_added = chai_ingredients.pop()  #Removing and returning the last element
print(f"last added ingredient: {last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")  #Reversing the list

chai_ingredients.sort() #sorting the list in ascending order

print(f"chai sorted ingredients: {chai_ingredients}")



sugar_levels = [1,2,3,4,5]

print(f"Maximum sugar level: {max(sugar_levels)}")  #Finding maximum value in the list
print(f"Minimum sugar level: {min(sugar_levels)}")  #Finding maximum value in the list


#operator overloading


base_liquid = ["water", "milk"]	
extra_liquid = ["ginger"]

full_liquid_mix = base_liquid + extra_liquid  #Using + operator to combine two lists

print(f"full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea","water"]

print(f"strong brew: {strong_brew * 3}")  #Using * operator to repeat the list elements


raw_spice_Data = bytearray(b"CINNAMON")

raw_spice_Data = raw_spice_Data.replace(b"CINNA", b"CARDA")  #Modifying bytearray data

print(f"Raw Spice Data: {raw_spice_Data}")

