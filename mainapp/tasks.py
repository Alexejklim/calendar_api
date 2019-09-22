from django.core.mail import send_mail
from mainapp.celery import app
from readconfig import email as system_email

@app.task
def send_notification_email(email, data):
    try:
        send_mail(
            data['event_name'],
            'Notification about event {0} in {1}'.format(data['event_name'], data['startdatetime']),
            system_email['login'],
            [email],
            fail_silently=False,
        )
    except:
        pass
