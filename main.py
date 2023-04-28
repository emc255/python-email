import email
import imaplib
import os
import smtplib

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def sending_email():
    smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    smtp_object.login(EMAIL, PASSWORD)
    from_address = EMAIL
    to_address = EMAIL
    subject = input("Enter Subject Line: ")
    message = input("Enter Message: ")
    msg = f"Subject: {subject} \n{message}"
    smtp_object.sendmail(from_address, to_address, msg)
    smtp_object.quit()


def reading_email():
    M = imaplib.IMAP4_SSL("imap.gmail.com")
    M.login(EMAIL, PASSWORD)
    print(M.list())
    M.select("inbox")
    typ, data = M.search(None, 'SUBJECT "jess"')
    print(f"TYPE: {typ}")
    print(f"DATA: {data}")

    email_id = data[0]
    result, email_data = M.fetch(email_id, "(RFC822)")
    print(f"RESULT: {result}")
    print(f"EMAIL DATA: {email_data}")
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode("utf-8")
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body)


def divider(title: str):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    # divider("sending email")
    # sending_email()

    divider("reading email")
    reading_email()
