import smtplib
import requests
from django.http import HttpResponse

class sendmailclass():
    def sendmailfunc(user, password, frommail, tomail, subjecttext, bodytext):
        gmail_user = user
        gmail_password = password

        sent_from = frommail
        to = [tomail]  
        subject = subjecttext
        print(bodytext)
        body = str(bodytext) #"Hey, what's up?\n\n- You"
        print(body)

        email_text  = "Subject: {}\n\n{}".format(subject, body)

        # email_text = """
        # From: %s  
        # To: %s  
        # Subject: %s

        # %s
        # """ % (sent_from, ", ".join(to), subject, body)

        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            print("establish connection successful")
            server.ehlo()
            print("identification successful")
            server.login(gmail_user, gmail_password)
            print("login successful")
            server.sendmail(sent_from, to, email_text)
            print("send mail successful")
            server.close()
            print('Email sent!')
            return HttpResponse("Successful!")
        except:  
            print('Something went wrong...')
            return HttpResponse("Failed")
