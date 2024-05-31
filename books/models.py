from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Books(models.Model):
    CATEGORY_BOOKS = (
        ("Художественная литература", "Художественная литература"),
        ("Информационная технология", "Информационная технология"),
        ("Деловая литература", "Деловая литература"),
        ("Юридическая литература", "Юридическая литература"),
        ("Наука, образование", "Наука, образование"),
        ("Языкознание, иностранные языки", "Языкознание, иностранные языки"),
        ("Школьные учебники", "Школьные учебники"),
        ("Детская литература", "Детская литература"),
        ("Медицина, спорт, здоровье", "Медицина, спорт, здоровье"),
        ("Другое", "Другое"),
    )

    title = models.CharField(
        max_length=50, verbose_name="Напишите название книги", null=True
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите фото", blank=True
    )
    description = models.TextField(verbose_name="Краткое описание")
    audio = models.FileField(
        upload_to="audio/", verbose_name="Загрузите аудио файл", blank=True
    )
    category_books = models.CharField(
        max_length=100, choices=CATEGORY_BOOKS, verbose_name="Выберите категорию"
    )

    audio_time = models.PositiveIntegerField(
        verbose_name="Укажите длительность аудио книг"
    )
    author = models.CharField(max_length=100, verbose_name="Укажите автора", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "книги"
        verbose_name_plural = "список книг"


class Review(models.Model):
    review_book = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name="review_book"
    )
    stars = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_book}-{self.stars}"

    class Meta:
        verbose_name = "отзывы"
        verbose_name_plural = "отзывы"
