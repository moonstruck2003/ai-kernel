# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing: ", order)


# prepare_chai(chai)
# print(chai)


chai = [1,2,3]

def edit_chai(cup):
    cup[1]=42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk,sugar)

make_chai("Darjeeling","YES","LOW") #positinal
make_chai(tea="green", milk="medium",sugar="high" ) #keywords 


def speical_chai(*ingredients, **extras): #key value argument , if input is not fixed, we can pass many parameters we can
    print("Ingredients",ingredients )
    print("extras", extras)

speical_chai("Cinemon","Cardamom",sweetner="honey",foam="yes")


# def chai_orders(order=[]):
#     order.append("Masala")
#     print(order)

def chai_orders(order=None):
    if order is None:
        order= []

chai_orders()
chai_orders()