import threading                                                        # Импортируем модуль для работы с потоками
import random                                                           # Импортируем модуль для случайных чисел
import time                                                             # Импортируем модуль для работы со временем

class Bank:                                                             # Определяем класс Bank
    def __init__(self):
        self.balance = 0                                                # Инициализируем баланс банка
        self.lock = threading.Lock()                                    # Создаем Lock для блокировки потоков

    def deposit(self):                                                  # Метод для пополнения средств
        for i in range(100):                                            # Цикл на 100 транзакций пополнения
            amount = random.randint(50, 500)                      # Генерируем случайную сумму для пополнения

            with self.lock:                                             # Защита кода блокировкой
                self.balance += amount                                  # Увеличиваем баланс на сгенерированную сумму
                print(f'Пополнение: {amount}. Баланс: {self.balance}')  # Выводим информацию о пополнении
                if self.balance >= 500:                                 # Если баланс >= 500, разблокируем
                    pass

            time.sleep(0.001)                                           # Имитация времени выполнения операции

    def take(self):
        for i in range(100):                                            # Цикл на 100 транзакций снятия
            amount = random.randint(50, 500)                      # Генерируем случайную сумму для снятия
            print(f'Запрос на {amount}')                                # Выводим сообщение о запросе

            with self.lock:                                             # Защита кода блокировкой
                if amount <= self.balance:                              # Проверяем, достаточно ли средств для снятия
                    self.balance -= amount                              # Уменьшаем баланс на запрашиваемую сумму
                    print(f'Снятие: {amount}. Баланс: {self.balance}')  # Выводим информацию о снятии
                else:
                    print('Запрос отклонён, недостаточно средств')      # Сообщаем об отказе в снятии

            time.sleep(0.001)                                           # Имитация времени ожидания

bk = Bank()                                                             # Создаем объект класса Bank

th1 = threading.Thread(target=bk.deposit)                               # Создаем потоки для deposit
th2 = threading.Thread(target=bk.take)                                  # Создаем потоки для take

th1.start()                                                             # Запускаем поток пополнения
th2.start()                                                             # Запускаем поток снятия

th1.join()                                                              # Ожидаем завершения потока пополнения
th2.join()                                                              # Ожидаем завершения потока снятия

print(f'Итоговый баланс: {bk.balance}')                                 # Выводим итоговый баланс