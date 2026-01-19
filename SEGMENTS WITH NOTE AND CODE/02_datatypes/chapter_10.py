chai_order = dict(type="Masala Chai",size="Large",sugar_level=2)

print(f"chai order: {chai_order}")


chai_recipe = {}

chai_recipe["base"] = "black_tea"

chai_recipe["liquid"] = "Milk"


print(f"Chai Recipe Base: {chai_recipe['base']}")


del chai_recipe["liquid"]  #Removing an item from the dictionary

print(f"Chai Recipe after deletion: {chai_recipe}")


#Membership test

print(f"Is suger in the order? : {'sugar_level' in chai_order}")  #Using 'in' to check key presence in dictionary


chai_order = dict(type="Ginger Chai",size="Medium",sugar_level=1)


# print(f"Order Details (keys) {chai_order.keys()}")

# print(f"Order Details (vales) {chai_order.values()}")

# print(f"Order Details (items ) {chai_order.items()}")


last_item = chai_order.popitem()  #Removing and returning the last inserted item
print(f"Last item removed: {last_item}")

extra_spices = {"cardamom":"crushed", "ginger":"sliced"}

chai_recipe.update(extra_spices)  #Updating dictionary with another dictionary

print(f"updated chai recipe: {chai_recipe}")


customer_note = chai_order.get("size","No Note") #Getting value with default if key not found, it doesnt crash , in chai_order["size"] it will crash if key not found

print(f"Customer noote: {customer_note}")