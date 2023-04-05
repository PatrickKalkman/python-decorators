def my_parameterized_decorator(arg1, arg2):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator_function


@my_parameterized_decorator("Hello", "World")
def my_function():
    print("Inside the function")


my_function()
