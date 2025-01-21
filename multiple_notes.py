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

# Функция добавления новой заметки.
def add_note():
    username = input("Введите имя пользователя: ")
    if not username: # Проверка на наличие имени,
        print("Имя пользователя не может быть пустым")
        return
    title = add_titles()
    if not title: # заголовков
        print("Заголовок не может быть пустым")
        return
    content = input("Введите небольшое описание заметки: ")
    if not content: # и описания.
        print("Описание не может быть пустым")
        return
    status = input("Введите статус заметки (Например: Выполнено/В процессе/Отложено): ")
    # Даты проверяются через функцию с пользовательским вводом
    created_date = user_date("Введите дату создания заметки в формате DD-MM-YYYY: ")
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
        print("Пока заметок нет.")
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

notes = [] # Список, содержащий заметки в виде словарей.
print("\t\t\tПриветствую в менеджере заметок!\n|Здесь вы можете работать с заметками. Обращайте внимание на подсказки.|")
while True:
    choice = input("\n0. Вывести список заметок\n1. Добавить заметку\nВведите цифру: ")
    if choice == "1":
        note = add_note() # Вызов внесения содержания заметки
        if note:
            notes.append(note) # Добавление заметки в список
    elif choice == "0":
        break
    else:
        print("Данной команды не существует, выберите из предложенного списка")
show_note(notes) # Вывод списка заметок