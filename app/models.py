from django.db import models
from solo.models import SingletonModel


# Create your models here.

class AboutUs(SingletonModel):
    text = models.TextField()

    def __str__(self):
        return self.text


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='الأسم')

    def __str__(self):
        return self.name


class ImageCity(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/cities/')
    default = models.BooleanField(default=False)


class Village(models.Model):
    name = models.CharField(max_length=255, verbose_name='الأسم')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city', verbose_name='المدينة')
    des = models.TextField()

    def __str__(self):
        return self.name


class ImageVillage(models.Model):
    name = models.CharField(max_length=255)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/villages/')
    default = models.BooleanField(default=False)
