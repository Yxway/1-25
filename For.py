for i in range(1, 11):
    print(i)

for i in range(2, 51, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

n = int(input("Введите число n: "))
total_sum = 0  
for i in range(1, n + 1):
    total_sum += i  
print(f"Сумма чисел от 1 до {n} равна: {total_sum}")

n = int(input("Введите число n: "))
factorial = 1  
for i in range(1, n + 1):
    factorial *= i 
print(f"Факториал числа {n} равен: {factorial}")

n = int(input("Введите число n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


numbers = [5, -2, 3, 0, -7, 8, 10, -1, 4]
count = 0  
for num in numbers:
    if num > 0:  
        count += 1
print(f"Количество положительных чисел: {count}")

text = "Программирование на Python — это увлекательно"
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"  
count = 0
for char in text:
    if char in vowels: 
        count += 1
print(f"Количество гласных букв: {count}")

numbers = [15, 42, 8, 99, 23, 57]
max_num = numbers[0] 
for num in numbers:
    if num > max_num:  
        max_num = num 
print(f"Наибольший элемент: {max_num}")

for i in range(1, 10):        
    for j in range(1, 10):  
        print(f"{i * j:2}", end=" ") 
    print()  

# Словарь

students = {"Иван": 5, "Мария": 4, "Петр": 3}
print("Оценка Ивана:", students["Иван"])

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4        
my_dict["a"] = 100     
del my_dict["b"]        
print(my_dict)

my_dict = {"apple": 10, "banana": 20}
key = "orange" 
result = my_dict.get(key, "Нет такого ключа")
print(result)

my_dict = {"name": "Ivan", "age": 25, "city": "Moscow"}
print("Ключи:", list(my_dict.keys()))
print("Значения:", list(my_dict.values()))
print("Количество пар:", len(my_dict))

prices = {"Хлеб": 50, "Молоко": 80, "Сыр": 300}
for item, price in prices.items():
    print(f"Товар: {item}, Цена: {price}")

prices = {"Хлеб": 50, "Молоко": 80, "Сыр": 300, "Икра": 500}
total_sum = sum(prices.values())
most_expensive = max(prices, key=prices.get)
print(f"Сумма всех цен: {total_sum}")
print(f"Самый дорогой товар: {most_expensive}")

text = "привет, мир"
char_counts = {}
for char in text:
    
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print(char_counts)

text = "яблоко банан яблоко апельсин банан яблоко"
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("Частота слов:", word_counts)
most_frequent = max(word_counts, key=word_counts.get)
print("Самое частое слово:", most_frequent)

original = {"a": 1, "b": 2, "c": 3}
swapped = {}
for key, value in original.items():
    swapped[value] = key
print("Исходный:", original)
print("Перевернутый:", swapped)

countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
country_capitals = dict(zip(countries, capitals))
user_country = input("Введите название страны: ")
capital = country_capitals.get(user_country, "Столица не найдена (такой страны нет в словаре)")
print("Столица:", capital)