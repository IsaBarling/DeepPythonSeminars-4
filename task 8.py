def modify_variables():
    variables = locals()
    for var_name in variables:
        if var_name.endswith("s") and len(var_name) > 1:
            value = variables[var_name]
            new_var_name = var_name[:-1]
            variables[new_var_name] = value
            variables[var_name] = None

# Создание переменных
dogs = ["Labradors", "Golden Retrievers", "Bulldogs"]
cats = ["Persians", "Siameses", "Maine Coons"]
bird = "Parrot"

# Замена содержимого переменных
modify_variables()

# Вывод переменных
print(dogs)
print(cats)
print(bird)
