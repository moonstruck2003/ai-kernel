def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2: Elaichi Chai"
    yield "Cup 3: Ginger chai"


stall = serve_chai()

# for chup in stall:
#     print(chup)


def get_chai_list():
    return ["Cup1","Cup 2","cup 2"]

#generator function

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"


chai = get_chai_gen()

print(next(chai))
print(next(chai))