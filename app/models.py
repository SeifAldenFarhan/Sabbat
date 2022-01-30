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


class Donation(SingletonModel):
    text = models.TextField(verbose_name='النص')
    bank_info = models.TextField(verbose_name='معلوامات البنك')


class OralHistory(SingletonModel):
    text = models.TextField(verbose_name='النص')


class Embroidery(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    image = models.ImageField(upload_to='images/embroideries/', verbose_name='الصورة')
    description = models.TextField(verbose_name='النص')
    price = models.PositiveIntegerField(verbose_name='السعر')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    image = models.ImageField(upload_to='images/book/', verbose_name='الصورة')
    description = models.TextField(verbose_name='النص')
    price = models.PositiveIntegerField(verbose_name='السعر')

    def __str__(self):
        return self.name


class Herb(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    image = models.ImageField(upload_to='images/herb/', verbose_name='الصورة')
    description = models.TextField(verbose_name='النص')
    price = models.PositiveIntegerField(verbose_name='السعر')

    def __str__(self):
        return self.name


class Olive(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    image = models.ImageField(upload_to='images/olive/', verbose_name='الصورة')
    description = models.TextField(verbose_name='النص')
    price = models.PositiveIntegerField(verbose_name='السعر')

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    image = models.ImageField(upload_to='images/accessories/', verbose_name='الصورة')
    description = models.TextField(verbose_name='النص')
    price = models.PositiveIntegerField(verbose_name='السعر')

    def __str__(self):
        return self.name
# item => pic , short discreption , images ,long description , title8
# tre5 alsafawe => text , items
# visitPage => text
# courses => text , items
# docan => text , items
# alm3rd => text , items
