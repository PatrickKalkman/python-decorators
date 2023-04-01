def my_first_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_first_decorator
def hello_world():
    print("Hello, World!")

hello_world()
