def calculate_profit_loss(companies):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Проходим по каждой компании в словаре
    for company, data in companies.items():
        # Вычисляем сумму доходов и расходов
        total_income = sum(data)
        total_expenses = sum([x for x in data if x < 0])

        # Вычисляем прибыль
        profit = total_income + total_expenses

        # Проверяем, является ли компания прибыльной или убыточной
        is_profitable = profit >= 0

        # Добавляем результат в словарь
        results[company] = is_profitable

    # Проверяем, являются ли все компании прибыльными
    all_profitable = all(results.values())

    return all_profitable, results

# Пример использования функции
companies = {
    "Company A": [100, 200, -50, 300, 150],
    "Company B": [500, 100, 200, 50],
    "Company C": [50, 100, 200, -300, 400]
}

is_all_profitable, results = calculate_profit_loss(companies)
print("All companies profitable:", is_all_profitable)
print("Results:", results)
