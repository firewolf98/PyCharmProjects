import functools


def func_tools(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args=[float(arg) for arg in args]
        return float(function(*args,**kwargs))
    return wrapper

@func_tools
def mean(primo,secondo,*resto):
    numbers=(primo, secondo)+resto
    return sum(numbers)/len(numbers)





print(mean(3,'4.5',4))
