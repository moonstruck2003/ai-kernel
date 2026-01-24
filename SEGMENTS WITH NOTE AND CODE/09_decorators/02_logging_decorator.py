from functools import wraps 

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling: {func.__name__}")
        result = func(*args,**kwargs)
        print("Finishing Calling: {func.__name__}")
        return result
    return wrapper 

@log_activity 

def brew_chai(type):
    print(f"brewing {type} chai")

brew_chai("LMAO")