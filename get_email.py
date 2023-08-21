import re
import requests

from list_from_exel import read_website_column
from send_email import open_txt

#  данные для подключения к файлу эксель
file_path = "2gispars.xlsx"  # Укажите путь к вашему файлу Excel
sheet_name = "Sheet1"       # Укажите имя листа, на котором находится столбец
column_name = "Веб-сайт 1"  # Укажите название столбца


def load_email():
    """ ОСНОВНАЯ Функция собирает имейли с урлов и записывает их в файл output.txt
    ЗАПУСКАТЬ ЕЁ"""
    urls_all = read_website_column(file_path, sheet_name, column_name)
    email_list = []
    for url in urls_all:
        email_check = find_emails_on_website(url)  # Список с имейлами найдеными на сайтах

        if email_check:  # Если список не пустой то
            for email in email_check:  # перебираем список
                if email not in email_list:  # если значение нет в готовом списке мейлов, то
                    email_list.append(email)  # добавляем имей в готовый список

    with open('output.txt', 'w') as file:
        file.truncate(0)
        for item in email_list:
            file.write(str(item) + '\n')

    open_txt()

    return print('Operation complete, check file output.txt')


def find_emails_on_website(url):
    """функция поиска имейлов на url страницах"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        # Получаем содержимое страницы сайта
        response = requests.get(url, headers=headers)
        # Получаем содержимое страницы сайта
        if response.status_code != 200:
            print(f"Не удалось получить содержимое страницы {url}. Код ответа: {response.status_code}")
            print('Рекомендуем удалить сайт из поиска')
            return []

        # Определяем регулярное выражение для поиска адресов электронной почты
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

        # Находим все совпадения с регулярным выражением в содержимом страницы
        matches = re.findall(email_pattern, response.text)

        return matches
    # обработка ошибки
    except Exception as e:
        print(f"Произошла ошибка на сайте {url} при обращении к сайту: {e}")
        print('Рекомендуем удалить сайт из поиска')
        return []


load_email()