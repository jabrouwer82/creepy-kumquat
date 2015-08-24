from google.appengine.api import mail
from configuration import EMAIL

def send_mail(subject, message='', **kwargs):
  mail.send_mail_to_admins(EMAIL, subject, message, **kwargs)
