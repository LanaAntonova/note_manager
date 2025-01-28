from datetime import datetime # Подключение библиотеки
from colorama import init

# Функция добавления нескольких заголовков.
def add_titles():
    titles = []
    while True:
        title = input("\033[3;37mВведите заголовок (или оставьте пустым для завершения): \033[0m")
        if title != '':
            if title not in titles:
                titles.append(title.capitalize())
            else:
                print(f"\033[31mЗаголовок {title} уже существует.\033[0m")
        else:
            break
    str_titles = ", ".join(titles)
    return str_titles

# Функция получения текущей даты.
def today():
    date = datetime.now().strftime("%d-%m-%Y")
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
            print("\033[31mНеверный формат даты. Попробуйте ещё раз.\033[0m")
    return date

# Функция вычисления дедлайна в днях.
def difference_date(begin_date, end_date):
    return (end_date - begin_date).days

# Функция вывода в соответствии с количеством дней до дедлайна.
def check_deadline(end_date):
    days = int(difference_date(today(), end_date))
    if days < 0:
        days *= -1
        return (f"Внимание! Дедлайн истёк \033[1;31m{days} "
              f"{'дня' if 1 > days > 5 else 'день' if days == 1 else 'дней'} назад\033[0m.")
    elif days > 0:
        return (f"До дедлайна осталось \033[1;32m{days} "
              f"{'дня' if 1 < days < 5 else 'день' if days == 1 else 'дней'}\033[0m.")
    else:
        return ("Внимание! Дедлайн \033[1;33mсегодня\033[0m!")

# Функция выбора статуса из предложенных
def status_create():
    status = "Новая"
    status_dict = {0: "Новая", 1: "Выполнено", 2: "В процессе", 3: "Отложено"}  # Словарь со значениями статуса
    # Цикл выбора нового статуса.
    while True:
        print("\033[3;37mВыберите статус заметки:\033[0m")
        for key, value in status_dict.items():
            print(f"\033[33m\t{key}.\033[0m {value}")  # Вывод вариантов статуса.
        new_status = input("\033[36mВведите цифру : \033[0m")
        if not new_status:
            choice = input("\033[36mХотите оставить прежний статус?\033[0m"
                           "\n\t\033[33m1.\033[0m Да\n\t\033[33m2.\033[0m Нет\n\033[36mВведите цифру : \033[0m")
            if choice == "2":
                continue
            else:
                break
        # Проверка наличия статуса в словаре.
        if int(new_status) in status_dict.keys():
            status = status_dict[int(new_status)]
            break
        else:
            print("\033[31mВведенного статуса нет, попробуйте ещё раз.\033[0m")
    return status

# Функция добавления новой заметки.
def create_note():
    username = input("\n\033[3;37mВведите имя пользователя: \033[0m")
    if not username: # Проверка на наличие имени,
        print("\033[31m\tИмя пользователя не может быть пустым\033[0m")
        return
    title = add_titles()
    if not title: # заголовков
        print("\033[31m\tЗаголовок не может быть пустым\033[0m")
        return
    content = input("\033[3;37mВведите небольшое описание заметки: \033[0m")
    if not content: # и описания.
        print("\033[31m\tОписание не может быть пустым\033[0m")
        return
    status = status_create()
    # Даты проверяются через функцию с пользовательским вводом
    created_date = today()
    issue_date = user_date("\033[3;37mВведите дату истечения заметки (дедлайн) в формате DD-MM-YYYY: \033[0m")
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

# Функция показывает содержание заметки по 3 на страницу
def display_notes(notes, page):
    start_index = 0 + page * 3
    end_index = 3 + page * 3
    print(f"\n\033[35mСписок заметок (стр.{page + 1}):\n------------------------------\033[0m")
    # Вывод содержания
    for idx, note in enumerate(notes[start_index:end_index], start=1):
        deadline = check_deadline(note['issue_date']) # Вызов подсчета дней до дедлайна
        # Красивый формат дат.
        created_date = note['created_date'].strftime("%d %B")
        issue_date = note['issue_date'].strftime("%d %B")
        print(f"\033[36mЗаметка №{idx + page * 3}.\033[0m"
              f"\n\t\033[3;37mПользователь:\033[0m {note['username']}"
              f"\n\t\033[3;37mЗаголовки:\033[0m {note['title']}"
              f"\n\t\033[3;37mОписание:\033[0m {note['content']}"
              f"\n\t\033[3;37mСтатус:\033[0m {note['status']}"
              f"\n\t\033[3;37mДата создания:\033[0m {created_date}"
              f"\n\t\033[3;37mДата дедлайна:\033[0m {issue_date}\n{deadline}"
              f"\n\033[35m------------------------------\033[0m")

# Функция удаления заметки.
def delete_note(notes):
    # Выбор критерия удаления
    delete_choice = input("\n\033[36mУдалить заметку\033[0m"
                          "\n\t\033[33m1.\033[0m по имени пользователя"
                          "\n\t\033[33m2.\033[0m по заголовку"
                          "\n\033[36mВведите цифру: \033[0m")
    if delete_choice == '2': # Удаление заметки по заголовку
        title = input("\033[36mВведите заголовок заметки: \033[0m")
        # Поиск и удаление в списке словарей заметок с указанным заголовком
        notes[:] = [note for note in notes if title not in note['title']]
        print(f"\033[32mЗаметки с заголовком '{title}' удалены.\033[0m")
    elif delete_choice == '1': # Удаление заметки по имени пользователя
        username = input("\033[36mВведите имя пользователя заметки: \033[0m")
        # Поиск и удаление в списке словарей заметок с указанным пользователем
        notes[:] = [note for note in notes if username not in note['username']]
        print(f"\033[32mЗаметки пользователя '{username}' удалены.\033[0m")
    else:
        print("\033[31mДанной команды не существует, выберите из предложенного списка\033[0m")

# Функция обновления поля заметки, заданного пользователем
def update_note(note):
    # Выбор критерия для обновления
    update_choice = input("\n\033[36mКакой пункт хотите изменить?\033[0m"
                          "\n\033[33m1.\033[0m Пользователь"
                          "\n\033[33m2.\033[0m Заголовок"
                          "\n\033[33m3.\033[0m Описание"
                          "\n\033[33m4.\033[0m Статус"
                          "\n\033[33m5.\033[0m Дата создания"
                          "\n\033[33m6.\033[0m Дата дедлайна"
                          "\n\t\033[36mВведите цифру: \033[0m")
    if update_choice == '6': # Обновление даты дедлайна
        issue_date = user_date("\033[36mВведите новую дату истечения заметки (дедлайн) в формате DD-MM-YYYY: \033[0m")
        if not issue_date:
            print("\033[33m\tДата дедлайна осталась прежней\033[0m")
            return
        note.update({'issue_date': issue_date})
    elif update_choice == '5': # Обновление даты создания
        created_date = user_date("\033[36mВведите новую дату создания заметки в формате DD-MM-YYYY: \033[0m")
        if not created_date:
            print("\033[33m\tДата создания осталась прежней\033[0m")
            return
        note.update({'created_date': created_date})
    elif update_choice == '4': # Обновление статуса
        status = status_create()
        if not status:
            print("\033[33m\tСтатус остался прежним\033[0m")
            return
        note.update({'status': status.upper()})
    elif update_choice == '3': # Обновление описания
        content = input("\033[36mВведите новое описание заметки: \033[0m")
        if not content:
            print("\033[33m\tОписание осталось прежним\033[0m")
            return
        note.update({'content': content.capitalize()})
    elif update_choice == '2': # Обновление заголовков
        title = add_titles()
        if not title:
            print("\033[33m\tЗаголовок остался прежним\033[0m")
            return
        note.update({'title': title.title()})
    elif update_choice == '1': # Обновление имени пользователя
        username = input("\033[36mВведите имя пользователя заметки: \033[0m")
        if not username:
            print("\033[33m\tИмя пользователя осталось прежним\033[0m")
            return
        note.update({'username': username.title()})
    else:
        print("\033[31mДанной команды не существует, выберите из предложенного списка\033[0m")
    # Вывод заметки с новым значением
    created_date = note['created_date'].strftime("%d %B")
    issue_date = note['issue_date'].strftime("%d %B")
    print(f"\033[32mОбновленные данные:\033[0m\n\tПользователь: {note['username']}"
          f"\n\tЗаголовки: {note['title']}\n\tОписание: {note['content']}"
          f"\n\tСтатус: {note['status']}\n\tДата создания: {created_date}"
          f"\n\tДата дедлайна: {issue_date}")
    return note

notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': datetime.strptime('27-11-2024', "%d-%m-%Y"),
     'issue_date': datetime.strptime('30-11-2024', "%d-%m-%Y")},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': datetime.strptime('25-11-2024', "%d-%m-%Y"),
     'issue_date': datetime.strptime('01-12-2024', "%d-%m-%Y")},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': datetime.strptime('20-11-2024', "%d-%m-%Y"),
     'issue_date': datetime.strptime('26-11-2024', "%d-%m-%Y")},
    {'username': 'Василий', 'title': 'Важное', 'content': 'Написать заявление на отпуск', 'status': 'новая',
     'created_date': datetime.strptime('27-01-2025', "%d-%m-%Y"),
     'issue_date': datetime.strptime('30-01-2025', "%d-%m-%Y")},
    {'username': 'Настасья', 'title': 'Учеба', 'content': 'Начать курсовую', 'status': 'в процессе',
     'created_date': datetime.strptime('25-01-2025', "%d-%m-%Y"),
     'issue_date': datetime.strptime('01-02-2025', "%d-%m-%Y")},
    {'username': 'Оля', 'title': 'План работы', 'content': 'Подготовить вебинар', 'status': 'выполнено',
     'created_date': datetime.strptime('20-01-2025', "%d-%m-%Y"),
     'issue_date': datetime.strptime('26-02-2025', "%d-%m-%Y")}
] # Список, содержащий заметки в виде словарей.
print("\033[36m\t\t\tПриветствую в менеджере заметок!"
      "\n|Здесь вы можете работать с заметками. Обращайте внимание на подсказки.|\033[0m")
while True:
    choice = input("\n\033[33m0.\033[0m Выйти"
                   "\n\033[33m1.\033[0m Добавить заметку"
                   "\n\033[33m2.\033[0m Обновить заметку"
                   "\n\033[33m3.\033[0m Удалить заметку"
                   "\n\033[33m4.\033[0m Вывести список заметок"
                   "\n\t\033[36mВведите цифру: \033[0m")
    if choice == "4":
        if not notes:  # Проверка на наличие заметок
            print("\033[31m\n\tПока заметок нет.\033[0m")
            continue
        else:
            for num_page in range(int(len(notes) / 3)): # Формирование страницы по 3 заметки
                display_notes(notes, num_page)  # Вывод списка заметок
    elif choice == "3":
        if not notes:  # Проверка на наличие заметок
            print("\033[31m\n\tПока заметок нет.\033[0m")
            continue
        delete_note(notes)  # Удаление заметки
    elif choice == "2":
        if not notes:  # Проверка на наличие заметок
            print("\033[31m\n\tПока заметок нет.\033[0m")
            continue
        num_note = int(input("\n\033[36mВведите номер заметки: \033[0m"))
        note = notes[num_note - 1]
        notes[num_note - 1] = update_note(note)  # Обновление заметки
    elif choice == "1":
        note = create_note() # Вызов внесения содержания заметки
        if note:
            notes.append(note) # Добавление заметки в список
    elif choice == "0":
        break
    else:
        print("\033[31mДанной команды не существует, выберите из предложенного списка\033[0m")
