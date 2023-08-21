import smtplib
from datetime import time
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import ssl

SENDER_EMAIL = "testdomsaitov123@yandex.ru"
PASSWORD = "cjiuuitudkuqhzot"
SUBJECT = "Откидные рамки, защита от камер фото видеофиксации, антиплатон, весовой контроль"
MESSAGE = ("Приглашаем к сотрудничеству автомагазины, установочные центры, автосалоны, автосервисы, "
           "региональные автопредприятия, занимающиеся розничной и "
           "оптовой торговлей автомобильными аксессуарами!) "
           "В прикрепленном файле прайс при заключении договора на оптовое сотрудничество\n"
           "Тел\WhatsApp: +7-912-247-44-10\n"
           "https://avtoaksekb04.ru/opt\n"
           "Начните зарабатывать вместе с нами!")
FILE_PATH = "opt.pdf"  # Optional attachment


def send_emails(email):
    """функция отправляет имейл письмо с указанного адреса(нашего), подставляя нужный текст и тему письма"""

    # создаем тело письма из составляющих
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(MESSAGE, 'plain'))

    if FILE_PATH:  # файл прикрепляет при условии указания пути файла
        with open(FILE_PATH, "rb") as attachment:
            attached_file = MIMEApplication(attachment.read(), _subtype="pdf")
            attached_file.add_header('content-disposition', 'attachment', filename=FILE_PATH)
            msg.attach(attached_file)

    # отправляет письмo
    try:

        with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as server:  # указываем сервер и порт
            server.login(SENDER_EMAIL, PASSWORD)  # авторизуем почту с которой отправляем
            msg['To'] = email  # почта на которую отправляем
            server.sendmail(SENDER_EMAIL, email, msg.as_string())  # подключаемся к сервреу

            with open('sent_mail.txt', 'a') as file:  # записывваем адреса на которые успешно отправили письмо
                file.write(str(email) + '\n')

            print(f"Отправили письмо на {email}")  # сообщение об успешной отправки
    except Exception as e:  # обработка ошибки
        print(f"Письмо не отправлено на {email}: {e}")  # сообщение с ошибкой


def open_txt():
    try:
        with open('output.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                send_emails(line)
                print('Пауза 5 секунд')
                time.sleep(5)

    except FileNotFoundError:
        print(f"Файл output.txt не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


open_txt()