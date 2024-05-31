from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = "__all__"
