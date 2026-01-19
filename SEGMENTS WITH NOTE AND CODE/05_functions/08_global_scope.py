chai_type = "Plain"

def front_desk(): 
    def kitchen():
        global chai_type  #will call the global variable on top
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final chai type", chai_type)
