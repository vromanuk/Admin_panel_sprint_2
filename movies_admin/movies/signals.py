import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from movies.models import Person


@receiver(post_save, sender=Person)
def congratulatory(sender, instance: Person, created: bool, **kwargs):
    if created and instance.birth_date == datetime.date.today():
        print(f"У {instance.first_name} {instance.last_name} сегодня день рождения! 🥳")
