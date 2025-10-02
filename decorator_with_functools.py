import functools

def change_case(func):
    @functools.wraps(func)
    def my_inner(name):
        return func(name).upper()
    return my_inner

@change_case
def my_fun(name):
    return "Hello " + name

print(my_fun("vinu"))
print(my_fun.__name__)