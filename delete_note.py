# Функция показывает содержание заметки
def show_note(notes):
    if not notes: # Проверка на наличие заметок
        print("Пока заметок нет.")
        return
    # Вывод содержания
    for idx, note in enumerate(notes, start=1):
        print(f"\nЗаметка №{idx}."
              f"\n\tПользователь: {note['username']}"
              f"\n\tЗаголовки: {note['title']}"
              f"\n\tОписание: {note['content']}")

# Функция удаления заметки.
def delete_note(notes):
    if not notes: # Проверка на наличие заметок
        print("Пока заметок нет.")
        return
    # Выбор критерия удаления
    delete_choice = input("Удалить заметку\n\t1. по имени пользователя\n\t2. по заголовку"
                      "\nВведите соответствующую цифру: ")
    if delete_choice == '2': # Удаление заметки по заголовку
        title = input("Введите заголовок заметки: ")
        # Поиск в списке словарей заметок с указанным заголовком
        notes[:] = [note for note in notes if title not in note['title']]
        print(f"Заметки с заголовком '{title}' удалены.")
    elif delete_choice == '1': # Удаление заметки по имени пользователя
        username = input("Введите имя пользователя заметки: ")
        # Поиск в списке словарей заметок с указанным пользователем
        notes[:] = [note for note in notes if username not in note['username']]
        print(f"Заметки пользователя '{username}' удалены.")
    else:
        print("Данной команды не существует, выберите из предложенного списка")

# Список заметок для примера
notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю'
        },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену'
        },
        {
            'username': 'Ваня',
            'title': 'Отпуск',
            'content': 'Выбрать путевку'
        },
        {
            'username': 'Оля',
            'title': 'Важно',
            'content': 'Подготовить отчет'
        }
]
print("\t\t\tПриветствую в менеджере заметок!\n|Здесь вы можете работать с заметками. Обращайте внимание на подсказки.|")
show_note(notes)
while True:
    choice = input("\n0. Вывести список заметок\n1. Удалить заметку\nВведите цифру: ")
    if choice == "1":
        delete_note(notes)  # Удаление заметки
    elif choice == "0":
        show_note(notes)  # Вывод списка заметок
        break
    else:
        print("Данной команды не существует, выберите из предложенного списка")