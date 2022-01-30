# Generated by Django 4.0.1 on 2022-01-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_product_imagecity_city_and_more'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='village',
            name='des',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
