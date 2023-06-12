def calculate_bonus(names, salary, bonus):
    bonus_dict = {}

    # Проходим по каждому элементу списков одновременно
    for name, sal, bns in zip(names, salary, bonus):
        # Извлекаем процент премии из строки
        percent = float(bns.rstrip('%'))

        # Рассчитываем сумму премии
        bonus_amount = sal * percent / 100

        # Добавляем пару ключ-значение в словарь
        bonus_dict[name] = bonus_amount

    return bonus_dict

# Пример использования функции
names = ["Alice", "Bob", "Charlie"]
salary = [1000, 2000, 1500]
bonus = ["10.25%", "5%", "12.5%"]

result = calculate_bonus(names, salary, bonus)
print(result)
