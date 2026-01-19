def serve_chai():
    chai_type = "Masala" # Local Scope
    print(f"inside function : {chai_type}")
chai_type = "Lemon"
serve_chai()
print(f"outside function: {chai_type}")


def chai_counter():
    chai_order = "Lemon" #Enclosing scope
    
    def chai_order():
        chai_order = "Ginger" 
        print(f"Inner: ", chai_order)
    chai_order()
    print("outer:", chai_order)

chai_order = "Tulsi" #Global 

chai_counter()
print("Global : ",chai_order)

