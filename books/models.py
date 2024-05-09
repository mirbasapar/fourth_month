from django.db import models


class PostBooks(models.Model):
    CATEGORY_BOOKS = (
        ('Художественная литература', 'Художественная литература'),
        ('Информационная технология', 'Информационная технология'),
        ('Деловая литература', 'Деловая литература'),
        ('Юридическая литература', 'Юридическая литература'),
        ('Наука, образование', 'Наука, образование'),
        ('Языкознание, иностранные языки', 'Языкознание, иностранные языки'),
        ('Школьные учебники', 'Школьные учебники'),
        ('Детская литература', 'Детская литература'),
        ('Медицина, спорт, здоровье', 'Медицина, спорт, здоровье'),
        ('Другое', 'Другое'),
    )

    title = models.CharField(max_length=50, verbose_name='Напишите название книги', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', blank=True)
    description = models.TextField(verbose_name='Краткое описание')
    audio = models.FileField(upload_to='audio/', verbose_name='Загрузите аудио файл', blank=True)
    category_books = models.CharField(max_length=100, choices=CATEGORY_BOOKS, verbose_name='Выберите категорию')

    audio_time = models.PositiveIntegerField(verbose_name='Укажите длительность аудио книг')
    author = models.CharField(max_length=100, verbose_name='Укажите автора', null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} - {self.created_at}'


    class Meta:
        verbose_name = 'книг'
        verbose_name_plural = 'список книг'
# Create your models here.
