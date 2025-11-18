def greet(user, /, *, text="Hello", **kwargs):
    print(f"{text} {user}")
    print(kwargs)



# text became kw-only - keyword only
greet("Frank", text="Gamarjoba", age=37, last_name="Washington")
