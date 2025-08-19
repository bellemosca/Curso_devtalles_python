global_var = "Sou global"


def outer_function():
    enclosing_var = "Sou enclosing"

    def inner_function():
        local_var = "Sou local"

        print(global_var)
        print(enclosing_var)
        print(local_var)

    inner_function()


outer_function()
