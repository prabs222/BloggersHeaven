from django.core.mail import send_mail
from django.conf import settings
def registration_mail(email):
    try:
        subject = 'Registered successfully to Bloggers Heaven!'
        message = 'Welcome to Bloggers Heaven! You have been successfully registered!'
        email_from = settings.EMAIL_HOST
        send_mail(subject, message,email_from,[email])
        print("sent email")
    except Exception as e:
        print(e)
        
        
        
        