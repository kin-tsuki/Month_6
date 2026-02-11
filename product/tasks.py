from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from product.models import Category
from decouple import config


@shared_task
def send_report():
    categories = Category.objects.all()
    report = []
    for category in categories:
        products_count = category.products.count()
        report.append(f'Category: {category.name} - Products count: {products_count}')
    
    report_text = '\n'.join(report)

    send_mail(
        "Monthly report",
        f"{report_text}",
        settings.EMAIL_HOST_USER,
        [config("ADMIN_EMAIL")],
        fail_silently=False,
    )