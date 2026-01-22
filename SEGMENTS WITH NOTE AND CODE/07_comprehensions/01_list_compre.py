menu = [
    "Masala Chai",
    "Espresso tea",
    "Cappuccino",
    "Latte",
    "Mocha",
    "Espresso tea"
]

espresso = [my_tea for my_tea in menu if len(my_tea) < 12]


print(espresso)