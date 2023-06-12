def sum_of_digits(number):
    # Вычисляем сумму цифр числа
    return sum(int(digit) for digit in str(number))

def sort_by_digit_sum(numbers):
    # Сортируем список по убыванию суммы цифр
    numbers.sort(reverse=True, key=sum_of_digits)

# Пример использования функции
numbers = [123, 45, 6789, 0, 9876]
sort_by_digit_sum(numbers)
print(numbers)