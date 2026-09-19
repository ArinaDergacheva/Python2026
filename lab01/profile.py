surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
if age < 1 or age > 120:
    print("Ошибка: возраст должен быть от 1 до 120.")
else:
    favorite_subject = input("Введите любимый предмет: ")
    study_hours = float(input("Введите количество часов подготовки в неделю: "))
    if study_hours < 0:
        print("Ошибка: количество часов не может быть отрицательным.")
    else:
        age_in_four_years = age + 4
        hours_for_four_weeks = study_hours * 4
        hours_per_day = study_hours / 7

print()
print("Карточка студента")
print(f"Имя и фамилия: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age} лет")
print(f"Возраст через 4 года: {age_in_four_years} лет")
print(f"Любимый предмет: {favorite_subject}")
print(f"Подготовка в неделю: {study_hours:.2f} ч.")
print(f"Подготовка за 4 недели: {hours_for_four_weeks:.2f} ч.")
print(f"Подготовка в день: {hours_per_day:.2f} ч.")