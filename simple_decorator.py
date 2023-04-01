def my_first_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

def hello_world():
    print("Hello, World!")

hello_world = my_first_decorator(hello_world)
hello_world()
