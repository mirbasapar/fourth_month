from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (("Male", "Male"), ("Female", "Female"))


class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True)
    telegram = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone",
            "experience",
            "telegram",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
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
