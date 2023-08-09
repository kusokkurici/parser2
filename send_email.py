import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import openpyxl


def send_emails(sender_email, sender_password, subject, message_text, attachment_path=None):
    """функция отправляет имейл письмо с указанного адреса(нашего), подставляя нужный текст и тему письма"""
    # читает адрес из файла exel
    # wb = openpyxl.load_workbook(excel_file_path)
    # sheet = wb.active
    # email_column = "T"  # это колонка из ктр должен извлекаться емейл
    # email_addresses = [cell.value for cell in sheet[email_column] if cell.value]
    email_addresses = ['yaroslav66@list.ru']

    # создаем тело письма из составляющих
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_text, 'plain'))

    if attachment_path: # файл прикрепляет при условии указания пути файла
        with open(attachment_path, "rb") as attachment:
            attached_file = MIMEApplication(attachment.read(), _subtype="pdf")
            attached_file.add_header('content-disposition', 'attachment', filename=attachment_path)
            msg.attach(attached_file)

    # отправляет письмо
    for recipient_email in email_addresses:
        try:
            with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:  # указываем сервер и порт
                server.login(sender_email, sender_password)  # авторизуем почту с которой отправляем
                msg['To'] = recipient_email  # почта на которую отправляем
                server.sendmail(sender_email, recipient_email, msg.as_string())  # подключаемся к сервреу
                print(f"Email sent to {recipient_email}")  # сообщение об успешной отправки
        except Exception as e:  # обработка ошибки
            print(f"Failed to send email to {recipient_email}: {e}")  # сообщение с ошибкой

# тест
sender_email = "ipollyce@mail.ru"
sender_password = "zEue4aYNmLmh99aBGYMZ"
# excel_file_path = "тест.xlsx"
subject = "дратути"
message_text = "и вам не хворать"
attachment_path = None  # Optional attachment

send_emails(sender_email, sender_password, subject, message_text, attachment_path)
