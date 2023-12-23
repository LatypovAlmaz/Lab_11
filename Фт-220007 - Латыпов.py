import logging

logging.basicConfig(filename="Lab_11.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("Логи для теста")
d = {'Россия' : 'Москва', 'Канада' : 'Оттава', 'США' : 'Вашингтон',
     'Китай' : 'Пекин', 'Бразилия' : 'Бразилиа', 'Австралия' : 'Канберра',
     'Индия' : 'Нью-Дели', 'Аргентина' : 'Буэнос-Айрес',  'Казахстан' : 'Астана',
     'Алжир' : 'Алжир', 'Франция' : 'Париж', 'Испания' : 'Мадрид',
     'Италия' : 'Рим',  'Великобритания' : 'Лондон', 'Япония' : 'Токио'}

print('Режимы работы')
m1 = '1. Поиск столицы'
m2 = '2. Поиск страны'
print(m1)
print(m2)
while True:
    try:
        logging.info("Выбор режима работы")
        choice1 = input('Введите число 1 или 2: ')
        choice = int(choice1)
        if choice < 1 or choice > 2:
            print('Ошибка!!! Вы ввели неприавильное число')
            logging.error(f"Ошибка выбора режима работы, пользователь ввел - {choice}")
            continue
        break
    except ValueError:
        print('Введите число')
        logging.error(f"Ошибка выбора режима работы, пользователь ввел - {choice1}")
count = 1
while count == 1:
    if choice == 1:
        logging.info(f"Выбранный режим - {m1}")
        while True:
            try:
                logging.info("Запрос страны")
                country1 = input('Введите страну, столицу которой хотите найти - ')
                capital1 = d[country1.title()]
                print('Столица -', capital1)
                logging.info(f"Введенная страна - {country1}")
                logging.info(f"Выведенная столица - {capital1}")
                count = int(input('Введите 1 чтобы продолжить или 0 чтобы остановиться: '))
                if count == 1:
                    logging.info("Продолжение работы")
                elif count == 0:
                    logging.info("Остановка работы")
                break
            except NameError:
                print('Такой страны нет в списке')
                logging.error(f"Ошибка ввода страны, пользователь ввел - {country1}")
            except KeyError:
                print('Такой страны нет в списке')
                logging.error(f"Ошибка ввода страны, пользователь ввел - {country1}")
    if choice == 2:
        logging.info(f"Выбранный режим - {m2}")
        while True:
            try:
                logging.info("Запрос столицы")
                capital2 = input('Введите столицу, страну которой хотите найти - ')
                for i in d.keys():
                    if d[i] == capital2.title():
                        country2 = i
                print('Страна -', country2)
                logging.info(f"Введенная столица - {capital2}")
                logging.info(f"Выведенная страна - {country2}")
                count = int(input('Введите 1 чтобы продолжить или 0 чтобы остановиться: '))
                if count == 1:
                    logging.info("Продолжение работы")
                elif count == 0:
                    logging.info("Остановка работы")
                del country2
                break
            except NameError:
                print('Такой столицы нет в списке')
                logging.error(f"Ошибка ввода столицы, пользователь ввел - {capital2}")
            except KeyError:
                print('Такой столицы нет в списке')
                logging.error(f"Ошибка ввода столицы, пользователь ввел - {capital2}")
logging.info("")