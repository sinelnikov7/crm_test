import imaplib
import email
import time


def get_key():
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        # result, data = mail.search(None, "ALL")
        result, data = mail.search(None, 'UNSEEN')
        ids = data[0]
        print(ids)
        print(len(ids))
        print(trying)
        if len(ids) > 0:
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            key = message[-6:]
            print(email_message['Date'])
            return key
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                return 'Письмо не пришло'


def get_new_password():
    trying = 0
    while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
        mail.login('vouka8@yandex.by', 'xmlfafkxvimeijkx')
        mail.list()
        mail.select('inbox')
        # result, data = mail.search(None, "ALL")
        result, data = mail.search(None, 'UNSEEN')
        ids = data[0]
        # print(ids)
        # print(len(ids))
        # print(trying)
        if len(ids) > 0:
            id_list = ids.split()
            latest_email_id = id_list[-1]
            result, data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            message = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            splited = message.split('Пароль: ')[1]
            password = splited[0:9]
            print(email_message['Date'])
            return password
        else:
            time.sleep(1)
            trying += 1
            if  trying > 10:
                return 'Письмо не пришло'

print(get_new_password())
print(get_key())