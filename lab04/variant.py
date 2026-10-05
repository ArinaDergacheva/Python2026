n = int(input("Введите количество чисел: "))
count = 0
total = 0
for _ in range(n):
    number = int(input("Введите число: "))
    if 10 <= number <= 20:
        count += 1
        total += number

print("Количество:", count)
print("Сумма:", total)