# ========= 2.1 ================
# сумму чисел a и b;
a, b = int(input()), int(input())
print(a + b)
# разность чисел a и b;
print(a - b)
# произведение чисел a и b;
print(a * b)
# частное чисел a и b;
print(a / b)
# целую часть от деления числа a и b;
print(a // b)
# остаток от деления числа a и b;
print(a % b)
# корень квадратный a и b из суммы их 10-х степеней:
print((a ** 10 + b ** 10) ** 0.5)

# ============ ИМТ =================
def imt(m, h):
    res = m / (h ** 2)  # Используем квадрат роста

    if 18.5 <= res <= 25:
        otv = "Оптимальная масса"
    elif res < 18.5:
        otv = "Недостаточная масса"
    else:  # Этот блок будет выполнен, если res >= 25
        otv = "Избыточная масса"
    return otv

m, h = float(input()), float(input())

print(imt(m, h))

# Стоимость строки

def cena():
    st = len(s) * 60
    rub = st // 100
    kop = st % 100
    return print(f"{rub} р. {kop} коп.")
s = input()
#s = "Привет, как дела?!"
cena()

# Количество слов
a = input()
list = a.split()
print(len(list))

# Зодиак
goroskop = [
    "Дракон",
    "Змея",
    "Лошадь",
    "Овца",
    "Обезьяна",
    "Петух",
    "Собака",
    "Свинья",
    "Крыса",
    "Бык",
    "Тигр",
    "Заяц",
]
s = int(input())
w = (s - 2000) % 12
print(goroskop[w])

# Переворот числа
# Функция для разворота последних пяти цифр числа
def reverse_last_five_digits(number):
    # Преобразование числа в строку
    number_str = str(number)
    # Разворот последних пяти цифр
    reversed_part = number_str[-5:][::-1]
    # Соединение неизменной части с развернутой
    if len(number_str) > 5:
        result_str = number_str[:-5] + reversed_part
    else:
        result_str = reversed_part
    # Преобразование результата обратно в число и его возврат
    return int(result_str)

# Ввод числа пользователем
input_number = int(input())

# Вывод результата
print(reverse_last_five_digits(input_number))

# Standard American Convention
s = int(input())
print(f"{s:,.0f}")


# Задача Иосифа Флавия
def josephus_problem(n, k):
    if n == 1:
        return 1
    else:
        return (josephus_problem(n - 1, k) + k-1) % n + 1

# Входные данные
n = int(input())
k = int(input())

# Вывод результата
print(f"{josephus_problem(n, k)}")
