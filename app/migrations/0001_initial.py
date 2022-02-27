# Generated by Django 4.0.1 on 2022-02-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/accessories/', verbose_name='الصورة')),
                ('description', models.TextField(verbose_name='النص')),
                ('price', models.PositiveIntegerField(verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/book/', verbose_name='الصورة')),
                ('description', models.TextField(verbose_name='النص')),
                ('price', models.PositiveIntegerField(verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الأسم')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='النص')),
                ('bank_info', models.TextField(verbose_name='معلوامات البنك')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationInfo',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(verbose_name='المبلغ')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Embroidery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/embroideries/', verbose_name='الصورة')),
                ('description', models.TextField(verbose_name='النص')),
                ('price', models.PositiveIntegerField(verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='العنوان')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('desc', models.TextField(verbose_name='النص')),
                ('image', models.ImageField(upload_to='images/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/herb/', verbose_name='الصورة')),
                ('description', models.TextField(verbose_name='النص')),
                ('price', models.PositiveIntegerField(verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='MuseumPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='./images/Museum')),
                ('caption', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Olive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/olive/', verbose_name='الصورة')),
                ('description', models.TextField(verbose_name='النص')),
                ('price', models.PositiveIntegerField(verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='OralHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='النص')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='العنوان')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('desc', models.TextField(verbose_name='النص')),
                ('image', models.ImageField(upload_to='images/training/')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الأسم')),
                ('des', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='app.city', verbose_name='المدينة')),
            ],
        ),
        migrations.CreateModel(
            name='PanoramicPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='./images/village/PanoramicPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='PanoramicPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='./images/city/PanoramicPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PanoramicPhotoCity', to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='MiscellaneousPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/MiscellaneousPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='MiscellaneousPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/MiscellaneousPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/InstitutionPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/InstitutionPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='EventsPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/EventsPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='EventsPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/EventsPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='CharactersPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/CharactersPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='CharactersPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/CharactersPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='AerialPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/AerialPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='AerialPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/AerialPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='ActionsPhotoVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/village/ActionsPhotoVillage')),
                ('caption', models.CharField(max_length=255)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.village')),
            ],
        ),
        migrations.CreateModel(
            name='ActionsPhotoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/city/ActionsPhotoCity')),
                ('caption', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city')),
            ],
        ),
    ]
