chai_type = "Ginger"

def update_order():
    chai_type = "elachi"
    def kitchen():
        nonlocal chai_type #it will get the upper chai_type, inside to inside function 
        chai_type = "kesar"
    kitchen()
    print("after the kitchen update: ", chai_type)

update_order()