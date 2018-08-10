"""
To solve this mission you must use the SendGrid API Key (this video will explain how to create your own API Key). Check out these Python examples.

It all starts with your first email. Let’s try to send one.

Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.

Subject of the email should be "Welcome" and body simply "Hi, {name}" ({name} should be replaced by a user's name)

Input: Two arguments: email and a username.

Output: None. You should send an email. You don’t need to return anything.

send_email('a.lyabah@checkio.org', 'oduvan')
send_email('somebody@gmail.com', 'Some Body')
"""
import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'Registered key'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", BODY.format(name))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('user_email@somewhere.com', 'User name')
    print('Done')
