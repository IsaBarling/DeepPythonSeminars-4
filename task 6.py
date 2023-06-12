def calculate_sum(numbers, index1, index2):
    # Проверяем, чтобы index1 был меньше или равен index2
    if index1 > index2:
        index1, index2 = index2, index1

    # Определяем индексы начала и конца суммирования
    start_index = max(index1, 0)
    end_index = min(index2, len(numbers) - 1)

    # Считаем сумму чисел в указанном диапазоне
    total_sum = sum(numbers[start_index : end_index + 1])

    return total_sum

# Пример использования функции
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index1 = 2
index2 = 5

result = calculate_sum(numbers, index1, index2)
print(result)
