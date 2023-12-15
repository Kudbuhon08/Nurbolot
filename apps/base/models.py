from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to = 'logo/',
        verbose_name="Логотип сайта"
    )
    contact = models.CharField(
        max_length=25,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        null=True,blank=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на инстаграм"
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на ватсап"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на фейсбук"
    )
    youtube = models.URLField(
        verbose_name="Ссылка на ютуб"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройка сайта"

class Projects(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="фото"
    )
    urls = models.URLField(
        verbose_name="Ссылка на фото"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши проекты"
        verbose_name_plural = "Наш проект"

    
class Directors(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to='image_1/',
        verbose_name="Фото 1"
    )
    
    description = RichTextField(
        verbose_name = "Текст"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Обращение директоров"
        verbose_name_plural = "Обращение директоров"

