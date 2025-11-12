# global


def greet(name): # name parameter shadow global variable
    # local scope
    # name = "Local name"
    print(f"Hello {name}")
    print(f"{name}, how are you?")
    print(some_global_var)


def f():
    # local
    t = 7
    print(name, t)



name = "Nick"
some_global_var = 17

greet(name)
print(name)
f()
# print(x, t)
