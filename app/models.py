from django.contrib.contenttypes.models import ContentType
from django.db import models
from solo.models import SingletonModel


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name='العنوان')
    date = models.DateField(verbose_name='التاريخ')
    desc = models.TextField(verbose_name='النص')
    image = models.ImageField(upload_to='images/gallery/')


class Training(models.Model):
    title = models.CharField(max_length=255, verbose_name='العنوان')
    date = models.DateField(verbose_name='التاريخ')
    desc = models.TextField(verbose_name='النص')
    image = models.ImageField(upload_to='images/training/')


class AboutUs(SingletonModel):
    text = models.TextField()

    def __str__(self):
        return self.text


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='الأسم')

    def __str__(self):
        return self.name


class PanoramicPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='PanoramicPhotoCity')
    picture = models.ImageField(upload_to='./images/city/PanoramicPhotoCity')
    caption = models.CharField(max_length=255)


class AerialPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/AerialPhotoCity')
    caption = models.CharField(max_length=255)


class ActionsPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/ActionsPhotoCity')
    caption = models.CharField(max_length=255)


class EventsPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/EventsPhotoCity')
    caption = models.CharField(max_length=255)


class InstitutionPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/InstitutionPhotoCity')
    caption = models.CharField(max_length=255)


class CharactersPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/CharactersPhotoCity')
    caption = models.CharField(max_length=255)


class MiscellaneousPhotoCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/city/MiscellaneousPhotoCity')
    caption = models.CharField(max_length=255)


class Village(models.Model):
    name = models.CharField(max_length=255, verbose_name='الأسم')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city', verbose_name='المدينة')
    des = models.TextField()

    def __str__(self):
        return "{} -> {}".format(self.city.name, self.name)


class PanoramicPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='./images/village/PanoramicPhotoCity')
    caption = models.CharField(max_length=255)


class AerialPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/AerialPhotoVillage')
    caption = models.CharField(max_length=255)


class ActionsPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/ActionsPhotoVillage')
    caption = models.CharField(max_length=255)


class EventsPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/EventsPhotoVillage')
    caption = models.CharField(max_length=255)


class InstitutionPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/InstitutionPhotoVillage')
    caption = models.CharField(max_length=255)


class CharactersPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/CharactersPhotoVillage')
    caption = models.CharField(max_length=255)


class MiscellaneousPhotoVillage(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/village/MiscellaneousPhotoVillage')
    caption = models.CharField(max_length=255)


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


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class DonationInfo(models.Model):
    d_id = models.AutoField(primary_key=True)
    amount = models.PositiveIntegerField(verbose_name="المبلغ")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.d_id, self.amount)


class MuseumPhoto(models.Model):
    image = models.ImageField(upload_to='./images/Museum')
    caption = models.CharField(max_length=255)

# item => pic , short discreption , images ,long description , title8
# tre5 alsafawe => text , items
# visitPage => text
# courses => text , items
# docan => text , items
# alm3rd => text , items
