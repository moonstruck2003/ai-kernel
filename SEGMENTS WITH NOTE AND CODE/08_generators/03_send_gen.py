def chai_customer():
    print("What chai would you like? :")

    order = yield 
    while True:
        print(f"preparing : {order}")
        order =yield 


stall = chai_customer()
next(stall) #start the generator 

stall.send("Masala Chai")
stall.send("Lemom Chai")