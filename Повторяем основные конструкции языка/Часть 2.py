# Координатные четверти
# put your python code here
# Считываем количество точек
n = int(input())

# Инициализируем счетчики для каждой четверти
first_quarter = second_quarter = third_quarter = fourth_quarter = 0

# Считываем координаты точек и увеличиваем соответствующие счетчики
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        first_quarter += 1
    elif x < 0 and y > 0:
        second_quarter += 1
    elif x < 0 and y < 0:
        third_quarter += 1
    elif x > 0 and y < 0:
        fourth_quarter += 1
    # Точки на осях координат не учитываем

# Выводим результат
print(f"Первая четверть: {first_quarter}")
print(f"Вторая четверть: {second_quarter}")
print(f"Третья четверть: {third_quarter}")
print(f"Четвертая четверть: {fourth_quarter}")


# Больше предыдущего
# put your python code here
# Функция для подсчета количества чисел, которые больше предшествующего им в списке
def count_greater_than_previous(numbers):
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
    return count

# Чтение строки с числами из входных данных
input_string = input()

# Преобразование строки в список чисел
numbers = list(map(int, input_string.split()))

# Подсчет и вывод количества чисел, которые больше предшествующего им числа
result = count_greater_than_previous(numbers)
print(result)

# Назад, вперёд и наоборот
# put your python code here
# Функция для обмена местами соседних элементов списка
def swap_adjacent_elements(numbers):
    for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers

# Чтение строки с числами из входных данных
input_string = input()

# Преобразование строки в список чисел
numbers = list(map(int, input_string.split()))

# Обмен местами соседних элементов списка
swapped_numbers = swap_adjacent_elements(numbers)

# Вывод измененного списка
print(' '.join(map(str, swapped_numbers)))

# Сдвиг в развитии
# put your python code here
# Чтение строки с числами из входных данных
input_string = input()

# Преобразование строки в список чисел
numbers = list(map(int, input_string.split()))

# Проверка, что список не пустой
if numbers:
    # Выполнение циклического сдвига направо
    last_element = numbers.pop()  # Удаляем последний элемент
    numbers.insert(0, last_element)  # Вставляем его в начало списка

# Вывод измененного списка
print(' '.join(map(str, numbers)))

# Различные элементы
# put your python code here
# Чтение строки с числами из входных данных
input_string = input()

# Преобразование строки в список чисел
numbers = list(map(int, input_string.split()))

# Преобразование списка в множество для получения уникальных элементов
unique_numbers = set(numbers)

# Подсчет количества уникальных элементов
unique_count = len(unique_numbers)

# Вывод количества уникальных элементов
print(unique_count)

# Произведение чисел
# put your python code here
# Чтение количества чисел в наборе
n = int(input())

# Чтение самих чисел и формирование списка
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)

# Чтение проверяемого числа
target_product = int(input())

# Флаг для определения, найдено ли произведение
found = False

# Перебор всех пар чисел из набора
for i in range(n):
    for j in range(n):
        if i != j and numbers[i] * numbers[j] == target_product:
            found = True
            break
    if found:
        break

# Вывод результата
if found:
    print("ДА")
else:
    print("НЕТ")

# Камень, ножницы, бумага
# put your python code here
# Чтение выбора Тимура и Руслана
timur_choice = input().strip().lower()
ruslan_choice = input().strip().lower()

# Определение результата игры
if timur_choice == ruslan_choice:
    print("ничья")
else:
    if (timur_choice == "камень" and ruslan_choice == "ножницы") or \
       (timur_choice == "ножницы" and ruslan_choice == "бумага") or \
       (timur_choice == "бумага" and ruslan_choice == "камень"):
        print("Тимур")
    else:
        print("Руслан")

# Камень, ножницы, бумага, ящерица, Спок
# Чтение выбора Тимура и Руслана
timur_choice = input().strip().lower()
ruslan_choice = input().strip().lower()

# Словарь с победными комбинациями
winning_combinations = {
    "камень": ["ножницы", "ящерица"],
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "спок"],
    "ящерица": ["спок", "бумага"],
    "спок": ["ножницы", "камень"]
}

# Определение результата игры
if timur_choice == ruslan_choice:
    print("ничья")
elif ruslan_choice in winning_combinations[timur_choice]:
    print("Тимур")
else:
    print("Руслан")

# Орел и решка
# put your python code here
# Считываем строку текста
sequence = input().strip()

# Инициализация переменных для текущего и максимального количества подряд идущих Решек
current_streak = 0
max_streak = 0

# Проходим по всем символам строки
for char in sequence:
    if char == 'Р':
        # Увеличиваем текущую последовательность, если символ 'Р'
        current_streak += 1
        # Обновляем максимальную последовательность, если текущая больше
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        # Сбрасываем текущую последовательность, если символ 'О'
        current_streak = 0

# Выводим максимальную последовательность подряд идущих Решек
print(max_streak)

# Кремниевая долина
# Считываем количество холодильников
n = int(input().strip())

# Инициализируем список для хранения номеров зараженных холодильников
infected_fridges = []

# Функция для проверки наличия последовательности 'anton'
def is_infected(data):
    target = "anton"
    j = 0
    for char in data:
        if char == target[j]:
            j += 1
            if j == len(target):
                return True
    return False

# Проходим по всем строкам и проверяем каждую на зараженность
for i in range(1, n + 1):
    data = input().strip()
    if is_infected(data):
        infected_fridges.append(i)

# Выводим номера зараженных холодильников
print(" ".join(map(str, infected_fridges)))

# Роскомнадзор запретил букву а
def song_restriction(word):
    # Начальная строка
    initial_phrase = word + " запретил букву"
    # Алфавит без буквы 'ё'
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    # Проходим по буквам алфавита
    for letter in alphabet:
        if letter in initial_phrase:
            # Выводим текущую строку с запрещенной буквой
            print(f"{initial_phrase} {letter}")
            # Удаляем все вхождения этой буквы из строки
            initial_phrase = initial_phrase.replace(letter, "")
            # Убираем лишние пробелы
            initial_phrase = " ".join(initial_phrase.split())


# Считываем ввод
word = input().strip()
# Вызов функции с введенным словом
song_restriction(word)
