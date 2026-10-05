n = int(input("Введите количество чисел: "))
total = 0
positive_count = 0
maximum = int(input("Введите число: "))
total += maximum
if maximum > 0:
    positive_count += 1
for _ in range(n - 1):
    number = int(input("Введите число: "))
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print("Сумма:", total)
print("Количество положительных:", positive_count)
print("Максимум:", maximum)