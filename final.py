username = input("Введите имя пользователя: ")
title1 = input("Введите 1-ый заголовок заметки: ")
title2 = input("Введите 2-ой заголовок заметки: ")
title3 = input("Введите 3-ий заголовок заметки: ")
content = input("Введите небольшое описание заметки: ")
status = input("Введите статус заметки (Например: К исполнению/В работе/Выполнена): ")
created_date = input("Введите дату создания заметки в формате DD-MM-YYYY: ")
issue_date = input("Введите дату истечения заметки (дедлайн) в формате DD-MM-YYYY: ")

note = [username.title(), [title1.capitalize(), title2.capitalize(), title3.capitalize()],
        content.capitalize(), status.upper(), created_date, issue_date]

print(
f"\nИмя пользователя: {note[0]}",
f"\nЗаголовоки заметки: {note[1]}",
f"\nОписание заметки: {note[2]}",
f"\nСтатус заметки: {note[3]}",
f"\nДата создания заметки: {note[4][:5]}",
f"\nДата истечения заметки (дедлайн): {note[5][:5]}"
)