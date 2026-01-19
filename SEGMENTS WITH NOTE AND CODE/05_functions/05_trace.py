def add_vat(price,vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100,150,200]
for price in orders: 
    final = add_vat(price,10)
    print(f"origian: {price}, Final with vat: {final}")




