def print_words(text):
    words = text.split()  # Разбиваем текст на слова

    # Сортируем слова по кодировке Unicode
    words = sorted(words, key=lambda x: x.encode('utf-8'))

    # Определяем ширину поля для выравнивания
    max_width = max(len(word) for word in words)

    for i, word in enumerate(words, start=1):
        # Выравниваем слово по правому краю
        formatted_word = f'{i:2}. {word:>{max_width}}'
        print(formatted_word)

# Пример использования функции
text = "Hello, my name is Python. I love coding!"
print_words(text)
