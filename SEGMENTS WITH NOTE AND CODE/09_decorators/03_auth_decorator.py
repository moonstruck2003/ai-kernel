from functools import wraps 

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied, admin only")
            return None #returns nothing, sometimes if not given it can throw error
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventor(role):
    print("Access grandted to tea inventory")

access_tea_inventor("User")    
access_tea_inventor("admin")    