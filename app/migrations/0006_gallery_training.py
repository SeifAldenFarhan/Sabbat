# Generated by Django 4.0.1 on 2022-02-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contact'),
    ]

    operations = [
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
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='العنوان')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('desc', models.TextField(verbose_name='النص')),
                ('image', models.ImageField(upload_to='images/training/')),
            ],
        ),
    ]
