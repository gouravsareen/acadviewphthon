import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("gauravsareen0112@gmail.com")
to_email = Email("akshitasharma01111@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

