import sys 

from fractions import Fraction #    importing Fraction class from fractions module    
from decimal import Decimal as D #importing Decimal class and giving it an alias D


ideal_temp = 95.5 

current_temp = 95.49999999999999


print(f"Ideal Temp Type : {ideal_temp}")
print(f"Ideal Temp Type : {current_temp}")

print(f"Difference in Temp : {ideal_temp - current_temp}")


print(sys.float_info)
