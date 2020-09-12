import smtplib

sender = "sender@gmail.com"
recipient = "codewithtomi@gmail.com"
password = "sender_password"
subject = "Test email from Python"
text = "Hello from Python"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()
