status_dict = { 1 : "Выполнено", 2 : "В процессе", 3 : "Отложено"} # Словарь со значениями статуса
status = "В процессе"
print(f"Текущий статус заметки: {status}")
# Цикл выбора нового статуса.
while True:
    print("\nВыберите новый статус заметки:")
    for key, value in status_dict.items():
        print(f"{key}. {value}") # Вывод вариантов статуса.
    new_status = int(input("Введите цифру : "))
    # Проверка наличия статуса в словаре.
    if new_status in status_dict.keys():
        status = status_dict[new_status]
        break
    else:
        print("\nВведенного статуса нет, попробуйте ещё раз.")
print(f"\nСтатус заметки успешно обновлён на: {status}") # Вывод нового статуса.