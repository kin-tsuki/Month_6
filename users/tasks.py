from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings 
from users.models import CustomUser
from time import sleep


@shared_task
def send_otp(email, code):
    send_mail(
        "Регистрация на сайт",
        f"Ваш код подтверждения: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


@shared_task
def send_login_mail(email):
    sleep(20)
    send_mail(
        "Вход на сайт",
        "Вы вошли на сайт shop_api",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


@shared_task
def del_inactive_users():
    inactive_users = CustomUser.objects.filter(is_active=False)
    for user in inactive_users:
        user.delete()
 

