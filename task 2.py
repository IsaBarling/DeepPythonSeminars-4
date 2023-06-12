def unique_unicode_codes(text):
    # Создаем множество для хранения уникальных кодов Unicode
    unique_codes = set()

    # Проходим по каждому символу в строке и добавляем его код Unicode во множество
    for char in text:
        unique_codes.add(ord(char))

    # Сортируем список кодов Unicode в порядке убывания
    sorted_codes = sorted(unique_codes, reverse=True)

    return sorted_codes

# Пример использования функции
text = "Hello, World!"
codes = unique_unicode_codes(text)
print(codes)
