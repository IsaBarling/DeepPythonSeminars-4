def sort_by_digit_sum(numbers):
    sorted_numbers = sorted(numbers, key=lambda x: sum(int(digit) for digit in str(x)), reverse=True)
    return sorted_numbers

# Пример использования функции
numbers = [123, 45, 6789, 12, 98765]
sorted_numbers = sort_by_digit_sum(numbers)
print(sorted_numbers)
                                                                                                    