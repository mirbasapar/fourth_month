from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class CustomUser(User):
    GENDER = (("Male", "Male"), ("Female", "Female"))
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(
        default=18, validators=[MinValueValidator(5), MaxValueValidator(99)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    experience = models.PositiveIntegerField(default=0)
    telegram = models.CharField(max_length=50, default="@")
    club = models.CharField(max_length=100, default="Reader")


@receiver(post_save, sender=CustomUser)
def set_exp(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан пользователь создан")
        exp = instance.experience
        if exp < 1:
            instance.club = "Стажер"
        elif 1 <= exp <= 2:
            instance.club = "Младший специалист"
        elif 2 <= exp <= 3:
            instance.club = "Специалист"
        elif 3 <= exp <= 5:
            instance.club = "Ведущий специалист"
        elif 5 <= exp <= 10:
            instance.club = "Главный специалист"
        elif exp > 10:
            instance.club = "Руководитель"
        else:
            instance.club = "Должность не определен"
        instance.save()
