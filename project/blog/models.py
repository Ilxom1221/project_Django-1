from django.db import models
from django.urls import reverse

# Create your models here.


# Категория
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категорию')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



# Названые
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата изминения')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})



    class Meta:
        verbose_name = 'Названия'
        verbose_name_plural = 'Названии'

