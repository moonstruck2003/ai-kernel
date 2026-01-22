fav_chais = {
    "Masala Chai", "Green Tea","Masala Chai", "Lemon tea", "Green tea","Elaichi chai"
}

#unique_chai = {chai for chai in fav_chais } #will give the unique values autometically
unique_chai = {chai for chai in fav_chais} 
print(unique_chai)


recipies = {
    "Masala chai" : ["ginger","cardmom","clove"],
    "Elaichi chai" : ["cardmom","milk"],
    "Spicy chai" : ["ginger","black pepper", "pepper"]
}



unique_spices = {spice for ingredients in recipies.values() for spice in ingredients  }

print(unique_spices)