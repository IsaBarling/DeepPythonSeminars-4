def keyword_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str)):
            key = str(key)
        result[value] = key
    return result

# Пример использования функции
arguments_dict = keyword_arguments(a=1, b=2, c=3.14, d="hello")

print(arguments_dict)

