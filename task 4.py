def bubble_sort(numbers):
    n = len(numbers)

    # Проходим по всем элементам списка
    for i in range(n):
        # Флаг, показывающий, были ли произведены обмены на данной итерации
        swapped = False

        # Проходим по элементам с индексами от 0 до n-i-1
        # Последние i элементов уже будут отсортированы
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего элемента, меняем их местами
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        # Если на данной итерации не было произведено обменов, список уже отсортирован
        if not swapped:
            break

# Пример использования функции
numbers = [9, 2, 5, 1, 7, 3]
bubble_sort(numbers)
print(numbers)
