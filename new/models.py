from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    
    def __str__(self):
        return self.name

class NewArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    

    def __str__(self):
        return self.title
