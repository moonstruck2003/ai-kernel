users = [
    {"id": 1, "total" : 100, "coupon" : "p20"},
    {"id": 2, "total" : 145, "coupon" : "f10"},
    {"id": 3, "total" : 213, "coupon" : "p50"},

]

discounts = {
    "p20" : (0.2,0),
    "f10" : (0.5,0),
    "p50" : (0,10),

}

for user in users: 
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["token"]} and got dicounts of  rupees {discount}")