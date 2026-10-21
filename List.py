numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print("Множество:", unique_numbers)
print("Количество элементов:", len(unique_numbers))

s = {10, 20, 30}
s.add(40)
s.remove(20)  
print("Результат:", s)

set1 = {1, 2, 3}
set2 = {3, 4, 5} 
print("Объединение:", set1 | set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Пересечение:", set1 & set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
only_in_set1 = set1 - set2
only_in_set2 = set2 - set1
print("Только в первом:", only_in_set1)
print("Только во втором:", only_in_set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}  
print("Элементы ровно в одном множестве:", set1 ^ set2)

s = {10, 20, 30, 40}
x = 25
exists = x in s
print(f"Число {x} есть в множестве: {exists}")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)  
print("Первое множество — подмножество второго:", is_subset)

text = "программирование"
unique_chars = set(text)
print("Множество символов:", unique_chars)
print("Количество уникальных символов:", len(unique_chars))

list1 = [3, 1, 2, 3, 4]
list2 = [2, 3, 3, 5, 6]
common_elements = sorted(list(set(list1) & set(list2)))
print("Отсортированный список общих элементов:", common_elements)

t = (10, 20, 30, 40, 50)
first = t
last = t[-1]
middle = t[len(t)//2]
print(first, last, middle)

t = (1, 2, 3, 4, 5, 6, 7, 8)
first_two = t[:2]
last_two = t[-2:]
reversed_t = t[::-1]
print(first_two, last_two, reversed_t)

t = (5, 10, 3, 8, 1)
length = len(t)
total = sum(t)
minimum = min(t)
maximum = max(t)
print(length, total, minimum, maximum)

t = (1, 2, 3, 2, 4, 2)
x = 2
exists = x in t
count = t.count(x)
index = t.index(x) if exists else -1
print(exists, count, index)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print(combined)

t = (42,)
print(type(t))

t = ("Анна", 25, "Москва")
name, age, city = t
print(name, age, city)

a, b = 5, 10
a, b = b, a
print(a, b)

t = (1, 2, 3, 4)
new_t = t[:1] + (99,) + t[2:]
print(new_t)

t = (3, 1, 2, 3, 2, 4, 1)
unique_sorted = tuple(sorted(set(t)))
print(unique_sorted)