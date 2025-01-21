from datetime import datetime # Подключение библиотеки

# Функция получения текущей даты, не требует аргументов,
# соответственно возвращает текущую дату.
def today():
    date = datetime.now().strftime("%d-%m-%Y")
    print(f"Текущая дата: {date}")
    date = datetime.strptime(date, "%d-%m-%Y")
    #print(type(date))
    return date

# Функция обработки пользовательского ввода, не требует аргументов,
# возвращает пользовательский ввод в виде даты
def user_date():
    while True:
        issue_date = input("Введите дату истечения заметки (дедлайн) в формате DD-MM-YYYY: ")
        try:
            issue_date = datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Неверный формат даты. Попробуйте ещё раз.")
    return issue_date

# Функция вычисления дедлайна в днях, в качестве аргументов идут две даты,
# на выходе получаем разницу между датами в днях.
def difference_date(begin_date, end_date):
    return (end_date - begin_date).days

# Вызов функции вычисления дедлайна в днях,
# в качестве аргументов используются результаты функций
# получения текущей даты и обработки пользовательского ввода.
days = int(difference_date(today(), user_date()))
# Выбор вывода в соответствии с количеством дней до дедлайна.
if days < 0:
    days *= -1
    print(f"Внимание! Дедлайн истёк {days} "
          f"{'дня' if 1 > days > 5 else 'день' if days == 1 else 'дней'} назад.")
elif days > 0:
    print(f"До дедлайна осталось {days} "
          f"{'дня' if 1 < days < 5 else 'день' if days == 1 else 'дней'}.")
else:
    print("Внимание! Дедлайн сегодня!")