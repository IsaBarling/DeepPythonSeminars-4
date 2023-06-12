def create_unicode_dict(numbers):
    # Разделяем строку с числами на отдельные значения
    num1, num2 = numbers.split()
    
    # Преобразуем числа в целочисленный тип данных
    num1 = int(num1)
    num2 = int(num2)

    # Определяем начальное и конечное значение диапазона
    start = min(num1, num2)
    end = max(num1, num2)

    # Создаем пустой словарь
    unicode_dict = {}

    # Проходим по каждому числу в диапазоне
    for num in range(start, end+1):
        # Получаем символ Unicode для текущего числа
        char = chr(num)
        # Добавляем пару ключ-значение в словарь
        unicode_dict[char] = num

    return unicode_dict

# Пример использования функции
numbers = input("Введите два числа через пробел: ")
unicode_dict = create_unicode_dict(numbers)
print(unicode_dict)
