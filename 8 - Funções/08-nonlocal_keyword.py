def outer():
    enclosing_var = "Enclosing variable"

    def inner():
        nonlocal enclosing_var
        enclosing_var = "Enclosing modificado"

    inner()
    print(enclosing_var)


outer()
