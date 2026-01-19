#SET


essential_spices = {"cardamom","ginger","cuinnamon"}

optional_spices = {"cloves","ginger","black pepper"}


all_spices = essential_spices.union(optional_spices)  #Combining two sets using union method

print(f"All Spices: {all_spices}")	


common_spices = essential_spices.intersection(optional_spices)  #Finding common elements using intersection method

print(f"Common Spices: {common_spices}")


only_in_essential = essential_spices - common_spices

print(f"Only in Essential Spices: {only_in_essential}")  #Finding difference between two sets


print(f" Its 'cloves' in essential spices? :{'cloves' in essential_spices}")  #in works with the set data type


#Frozen Set --> immutable frozen 

