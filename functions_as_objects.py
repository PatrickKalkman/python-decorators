def say_message_to_naomi(message_func):
    return message_func("Naomi")


def say_hello(name):
    print(f"Hello, {name}")


def say_goodbye(name):
    print(f"Goodbye, {name}")


say_message_to_naomi(say_hello)
say_message_to_naomi(say_goodbye)
