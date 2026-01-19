order_amount = int( input("Enter the order amount: "))

print(f"Order amopunt: {type(order_amount)}")

delivery_fees = 0 if order_amount>300 else 30 


print(delivery_fees)