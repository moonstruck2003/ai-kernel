# def make_chai():
#     #return "HHEre is your masala chai"
#     print("Here is a masala chai)

# return_value = make_chai()
# print(return_value)


def idle_chaiwala():
    pass

print(idle_chaiwala())


def sold_cups():
    return 102
total = sold_cups()
print(total)  # one value


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry chai over"

    return "chai is ready"  
    print("chai") #will never execture, early return 

print(chai_status(0))
print(chai_status(5))



def chai_report():
    return 100,20,10 #multi value return ]
sold,remaining, _ = chai_report()
print(sold,remaining)