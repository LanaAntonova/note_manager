from datetime import datetime # Подключение библиотеки

# Функция добавления нескольких заголовков.
def add_titles():
    titles = []
    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ")
        if title != '':
            if title not in titles:
                titles.append(title.capitalize())
            else:
                print(f"Заголовок {title} уже существует.")
        else:
            break
    str_titles = ", ".join(titles)
    return str_titles

# Функция получения текущей даты.
def today():
    date = datetime.now().strftime("%d-%m-%Y")
    # print(f"Текущая дата: {date}")
    date = datetime.strptime(date, "%d-%m-%Y")
    return date

# Функция обработки пользовательского ввода даты.
def user_date(str):
    while True:
        date = input(str)
        try:
            date = datetime.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            print("Неверный формат даты. Попробуйте ещё раз.")
    return date

# Функция вычисления дедлайна в днях.
def difference_date(begin_date, end_date):
    return (end_date - begin_date).days

# Функция вывода в соответствии с количеством дней до дедлайна.
def check_deadline(end_date):
    days = int(difference_date(today(), end_date))
    if days < 0:
        days *= -1
        return (f"Внимание! Дедлайн истёк {days} "
              f"{'дня' if 1 > days > 5 else 'день' if days == 1 else 'дней'} назад.")
    elif days > 0:
        return (f"До дедлайна осталось {days} "
              f"{'дня' if 1 < days < 5 else 'день' if days == 1 else 'дней'}.")
    else:
        return ("Внимание! Дедлайн сегодня!")

# Функция выбора статуса из предложенных
def status_create():
    status_dict = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}  # Словарь со значениями статуса
    # Цикл выбора нового статуса.
    while True:
        print("Выберите статус заметки:")
        for key, value in status_dict.items():
            print(f"\t{key}. {value}")  # Вывод вариантов статуса.
        new_status = int(input("Введите цифру : "))
        # Проверка наличия статуса в словаре.
        if new_status in status_dict.keys():
            status = status_dict[new_status]
            break
        else:
            print("\nВведенного статуса нет, попробуйте ещё раз.")
    return status

# Функция добавления новой заметки.
def create_note():
    username = input("\nВведите имя пользователя: ")
    if not username: # Проверка на наличие имени,
        print("\tИмя пользователя не может быть пустым")
        return
    title = add_titles()
    if not title: # заголовков
        print("\tЗаголовок не может быть пустым")
        return
    content = input("Введите небольшое описание заметки: ")
    if not content: # и описания.
        print("\tОписание не может быть пустым")
        return
    status = status_create()
    # Даты проверяются через функцию с пользовательским вводом
    created_date = today()
    issue_date = user_date("Введите дату истечения заметки (дедлайн) в формате DD-MM-YYYY: ")
    # Создание словаря, который содержит данные о заметки
    note = {
        'username': username.title(),
        'title': title.title(),
        'content': content.capitalize(),
        'status': status.upper(),
        'created_date': created_date,
        'issue_date': issue_date
    }
    return note

# Функция показывает содержание заметки
def show_note(notes):
    if not notes: # Проверка на наличие заметок
        print("\n\tПока заметок нет.")
        return
    # Вывод содержания
    for idx, note in enumerate(notes, start=1):
        deadline = check_deadline(note['issue_date']) # Вызов подсчета дней до дедлайна
        # Красивый формат дат.
        created_date = note['created_date'].strftime("%d %B")
        issue_date = note['issue_date'].strftime("%d %B")
        print(f"\nЗаметка №{idx}."
              f"\n\tПользователь: {note['username']}"
              f"\n\tЗаголовки: {note['title']}"
              f"\n\tОписание: {note['content']}"
              f"\n\tСтатус: {note['status']}"
              f"\n\tДата создания: {created_date}"
              f"\n\tДата дедлайна: {issue_date}"
              f"\n\t\t{deadline}")

# Функция удаления заметки.
def delete_note(notes):
    if not notes: # Проверка на наличие заметок
        print("\n\tПока заметок нет.")
        return
    # Выбор критерия удаления
    delete_choice = input("Удалить заметку\n\t1. по имени пользователя\n\t2. по заголовку"
                      "\nВведите соответствующую цифру: ")
    if delete_choice == '2': # Удаление заметки по заголовку
        title = input("Введите заголовок заметки: ")
        # Поиск и удаление в списке словарей заметок с указанным заголовком
        notes[:] = [note for note in notes if title not in note['title']]
        print(f"Заметки с заголовком '{title}' удалены.")
    elif delete_choice == '1': # Удаление заметки по имени пользователя
        username = input("Введите имя пользователя заметки: ")
        # Поиск и удаление в списке словарей заметок с указанным пользователем
        notes[:] = [note for note in notes if username not in note['username']]
        print(f"Заметки пользователя '{username}' удалены.")
    else:
        print("Данной команды не существует, выберите из предложенного списка")


notes = [] # Список, содержащий заметки в виде словарей.
print("\t\t\tПриветствую в менеджере заметок!\n|Здесь вы можете работать с заметками. Обращайте внимание на подсказки.|")
while True:
    choice = input("\n0. Выйти"
                   "\n1. Добавить заметку"
                   "\n2. Удалить заметку"
                   "\n3. Вывести список заметок\n\tВведите цифру: ")
    if choice == "3":
        show_note(notes)  # Вывод списка заметок
    elif choice == "2":
        delete_note(notes)  # Удаление заметки
    elif choice == "1":
        note = create_note() # Вызов внесения содержания заметки
        if note:
            notes.append(note) # Добавление заметки в список
    elif choice == "0":
        break
    else:
        print("Данной команды не существует, выберите из предложенного списка")
