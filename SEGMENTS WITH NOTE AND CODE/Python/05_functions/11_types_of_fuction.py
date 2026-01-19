def pure_chai(cups):
    return cups*10

total_chai = 0


#not recommended , impure functions 
def impure_chai(cups): 
    global total_chai
    total_chai +=cups

#recursive function 
def pour_chai(n):
    print(n)
    if n==0:
        return "All cups poured"
    return pour_chai(n-1)
print(pour_chai(3))


chai_types = ["light","karak","Ginger","karak"]

strong_chai = list(filter(lambda chai : chai!="karak",chai_types)) #We want to iterate nthe chai_types and only value we want out of there which is true( karak), condition: chai=="kadak"
print(strong_chai)
