username = input("Введите имя пользователя: ")
title = input("Введите название заметки: ")
content = input("Введите небольшое описание заметки: ")
status = input("Введите статус заметки (Например: К исполнению/В работе/Выполнена): ")
created_date = input("Введите дату создания заметки в формате DD-MM-YYYY: ")
issue_date = input("Введите дату истечения заметки (дедлайн) в формате DD-MM-YYYY: ")

print("Имя пользователя: ", username)
print("Заголовок заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status.lower())
print("Дата создания заметки: ", created_date[:5])
print("Дата истечения заметки (дедлайн): ", issue_date[:5])