# Функция поиска заметок.
def search_notes(notes, keyword=None, status=None):
    if not keyword and not status:
        print("\nПараметры поиска не введены.")
    # Поиск только по ключевому слову.
    elif keyword != None and not status:
        j = 0  # Счетчик заметок.
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # Временный список значения словаря.
            for k in range(len(cur_values)):  # Цикл проверки
                if keyword in cur_values[k]:  # наличия ключевого слова во временном списке.
                    j += 1
                    if j == 1:
                        print(f"\nПо слову '{keyword}' найдены заметки:"
                              f"\n\033[36mЗаметка{j}.\033[0m")
                    else:
                        print(f"\033[36mЗаметка{j}.\033[0m")
                    print(f"\t\033[3;37mПользователь:\033[0m {notes[i]['username']}"
                          f"\n\t\033[3;37mЗаголовки:\033[0m {notes[i]['title']}"
                          f"\n\t\033[3;37mОписание:\033[0m {notes[i]['content']}"
                          f"\n\t\033[3;37mСтатус:\033[0m {notes[i]['status']}"
                          f"\n\t\033[3;37mДата создания:\033[0m {notes[i]['created_date']}"
                          f"\n\t\033[3;37mДата дедлайна:\033[0m {notes[i]['issue_date']}")
        if j == 0:
            print(f"\nСлова '{keyword}' в заметках не существует.")
    # Поиск только по статусу.
    elif not keyword and status != None:
        j = 0
        for i in range(len(notes)):               # Цикл проверки
            if status == notes[i].get('status'):  # наличия статуса в словаре.
                j += 1
                if j == 1:
                    print(f"\nПо статусу '{status}' найдены заметки:"
                          f"\n\033[36mЗаметка {j}.\033[0m")
                else:
                    print(f"\033[36mЗаметка {j}.\033[0m")
                print(f"\t\033[3;37mПользователь:\033[0m {notes[i]['username']}"
                      f"\n\t\033[3;37mЗаголовки:\033[0m {notes[i]['title']}"
                      f"\n\t\033[3;37mОписание:\033[0m {notes[i]['content']}"
                      f"\n\t\033[3;37mСтатус:\033[0m {notes[i]['status']}"
                      f"\n\t\033[3;37mДата создания:\033[0m {notes[i]['created_date']}"
                      f"\n\t\033[3;37mДата дедлайна:\033[0m {notes[i]['issue_date']}")
        if j == 0:
            print(f"\nСтатуса '{status}' в заметках не существует.")
    # Поиск только по ключевому слову и статусу.
    else:
        j = 0
        for i in range(len(notes)):
            cur_values = list(notes[i].values())  # Временный список значения словаря.
            for k in range(len(cur_values)):                                       # Цикл проверки
                if keyword in cur_values[k] and status == notes[i].get('status'):  # наличия ключевого слова во временном списке и статуса в словаре.
                    j += 1
                    if j == 1:
                        print(f"\nПо слову '{keyword}' и статусу '{status}' найдены заметки:"
                              f"\n\033[36mЗаметка {j}.\033[0m")
                    else:
                        print(f"\033[36mЗаметка {j}.\033[0m")
                    print(f"\t\033[3;37mПользователь:\033[0m {notes[i]['username']}"
                          f"\n\t\033[3;37mЗаголовки:\033[0m {notes[i]['title']}"
                          f"\n\t\033[3;37mОписание:\033[0m {notes[i]['content']}"
                          f"\n\t\033[3;37mСтатус:\033[0m {notes[i]['status']}"
                          f"\n\t\033[3;37mДата создания:\033[0m {notes[i]['created_date']}"
                          f"\n\t\033[3;37mДата дедлайна:\033[0m {notes[i]['issue_date']}")

        if j == 0:
            print(f"\nНе найдены заметки со словом '{keyword}' и статусом '{status}'.")
    print("Поиск завершен.")

notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
search_notes(notes, keyword='покупок')
search_notes(notes, status='в процессе')
search_notes(notes, keyword='работы', status='выполнено')
search_notes(notes, keyword='принтер', status='в проекте')