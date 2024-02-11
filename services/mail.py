import imaplib
import email
import time
import quopri


def get_key():
    """Получение кода подтверждения при восстановлении пароля из почты"""
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, 'UNSEEN')
        for m in data[0].split(): # Обработка каждого найденного письма
            result, message_data = mail.fetch(m, "(RFC822)")
            if result == "OK":
                raw_email = message_data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                try:
                    topic = email_message['Subject'].replace("=?utf-8?Q?", '').replace('?', '')
                    topic = quopri.decodestring((topic)).decode('utf-8').replace(' ', '')
                except Exception:
                    continue
                if topic == 'Восстановление_пароля':
                    message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
                    key = message[-6:]
                    return key
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                return 'Письмо не пришло'

def get_new_password():
    """Получение нового пароля из почты"""
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, 'UNSEEN')
        for m in data[0].split(): # Обработка каждого найденного письма
            result, message_data = mail.fetch(m, "(RFC822)")
            if result == "OK":
                raw_email = message_data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                try:
                    topic = email_message['Subject'].replace("=?utf-8?Q?", '').replace('?', '')
                    topic = quopri.decodestring((topic)).decode('utf-8').replace(' ', '')
                except Exception:
                    continue
                if topic == 'Изменение_логина_или_пароля':
                    message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
                    splited = message.split('Пароль: ')[1]
                    password = splited[0:9]
                    print(password)
                    return password
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                print('@@@@@@@')
                return 'Письмо не пришло'

# get_new_password()
# get_key()
