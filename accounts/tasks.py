# from core.celery import APP
#
from .utils import send_sms
#
#
# @APP.task()
# def send_phone_notification(user_data):
#     send_sms(user_data['message'], user_data['phone'])


from celery import shared_task
from django.core.mail import send_mail
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# @shared_task
# def create_random_user_accounts(total):
#     for i in range(total):
#         username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
#         email = '{}@example.com'.format(username)
#         password = get_random_string(50)
#         User.objects.create_user(username=username, email=email, password=password)
#     return '{} random users created with success!'.format(total)


@shared_task
def send_phone_notification(user_data):
    send_sms(user_data['message'], user_data['phone'])