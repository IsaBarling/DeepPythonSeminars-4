TAX_THRESHOLD = 5000000
WITHDRAWAL_FEE_PERCENTAGE = 1.5
WITHDRAWAL_FEE_MIN = 30
WITHDRAWAL_FEE_MAX = 600
INTEREST_RATE = 0.03

def atm_program():
    balance = 0
    withdrawal_count = 0
    deposit_count = 0
    tax_collected = 0
    fee_collected = 0
    transaction_history = []

    print("Добро пожаловать в банкомат компании Tencent's")
    print("============================================")

    while True:
        print("Выберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            deposit_amount = get_deposit_amount()
            deposit(deposit_amount, balance, deposit_count, tax_collected, transaction_history)
            deposit_count += 1

        elif choice == "2":
            withdrawal_amount = get_withdrawal_amount()
            withdrawal(withdrawal_amount, balance, withdrawal_count, tax_collected, fee_collected, transaction_history)
            withdrawal_count += 1

        elif choice == "3":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

        print(f"Текущий баланс: {balance} у.е.")

    print("============================================")
    print("Мини-чек:")
    print(f"Сумма налогов: {tax_collected} у.е.")
    print(f"Сумма комиссий: {fee_collected} у.е.")
    print("Спасибо за использование банкомата компании Tencent's!")
    print("История транзакций:")
    print(transaction_history)

def get_deposit_amount():
    while True:
        deposit_amount = int(input("Введите сумму для пополнения: "))
        if deposit_amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50 у.е.")
        else:
            return deposit_amount

def get_withdrawal_amount():
    while True:
        withdrawal_amount = int(input("Введите сумму для снятия: "))
        if withdrawal_amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50 у.е.")
        else:
            return withdrawal_amount

def deposit(amount, current_balance, deposit_count, tax_collected, transaction_history):
    current_balance += amount
    transaction_history.append(f"Пополнение: +{amount} у.е.")

    if deposit_count % 3 == 0:
        interest = current_balance * INTEREST_RATE
        current_balance += interest
        transaction_history.append(f"Начисление процентов: +{interest} у.е.")

    if current_balance >= TAX_THRESHOLD:
        tax = current_balance * 0.1
        tax_collected += tax
        current_balance -= tax
        transaction_history.append(f"Списание налога: -{tax} у.е.")

def withdrawal(amount, current_balance, withdrawal_count, tax_collected, fee_collected, transaction_history):
    withdrawal_fee = amount * WITHDRAWAL_FEE_PERCENTAGE / 100
    withdrawal_fee = max(withdrawal_fee, WITHDRAWAL_FEE_MIN)
    withdrawal_fee = min(withdrawal_fee, WITHDRAWAL_FEE_MAX)
    amount += withdrawal_fee

    if amount > current_balance:
        print("Недостаточно средств на счете")
        return

    current_balance -= amount
    transaction_history.append(f"Снятие: -{amount} у.е.")

    if withdrawal_count % 3 == 0:
        interest = current_balance * INTEREST_RATE
        current_balance += interest
        transaction_history.append(f"Начисление процентов: +{interest} у.е.")

    if current_balance >= TAX_THRESHOLD:
        tax = current_balance * 0.1
        tax_collected += tax
        current_balance -= tax
        transaction_history.append(f"Списание налога: -{tax} у.е.")

    fee_collected += withdrawal_fee
    transaction_history.append(f"Комиссия за снятие: +{withdrawal_fee} у.е.")

atm_program()
