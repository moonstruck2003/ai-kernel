chai_type = "Ginger Chai"

customerr_name = "Priya"

print(f"order for {customerr_name} : {chai_type} please!" )


chai_description = "aromatic and Bold more" 

print(f"First Word: {chai_description[0:7:2]}")
print(f"First Word: {chai_description[:7]}")
print(f"Last Word: {chai_description[12:]}")

print(f"First Word: {chai_description[::-1]}")  #reversing the string using slicing

lable_Text = "Chai Sp^ecial"

encoded_label = lable_Text.encode("utf-8")  #encoding the string to bytes using utf-8 encoding

print(f"encoded label : {encoded_label}")

print(f"nonencoded label : {lable_Text}")

decoded_label = encoded_label.decode("utf-8")  #decoding the bytes back to string using utf-8 encoding

print(f"decoded label : {decoded_label}")