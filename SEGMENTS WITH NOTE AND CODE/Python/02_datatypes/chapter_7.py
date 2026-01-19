#TUPLE 




masala_spices = ("cardamom", "cinnamon", "cloves", "ginger")

(spice1,spice2,spice3,spice4)= masala_spices

print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}, {spice4}")


ginger_ration, cardamom_ratio = 2 , 1 

print(f"Ratio is G :{ginger_ration}, C:{cardamom_ratio}")

ginger_ration, cardamom_ratio,  = cardamom_ratio, ginger_ration #swapping values

print(f"Swapped Ratio is G :{ginger_ration}, C:{cardamom_ratio}")



#memvbership 

print(f"Is ginger in masala spices? : {'ginger' in masala_spices}") #in works with the tuple data type