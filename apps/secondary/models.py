from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Галерея"
        verbose_name_plural="Галерея"
