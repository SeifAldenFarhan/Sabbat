# Generated by Django 3.2.7 on 2022-05-31 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(default='Je', max_length=255, verbose_name='الأسم انجليزي'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actionsphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ActionsPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='actionsphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ActionsPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='aerialphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AerialPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='aerialphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AerialPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='charactersphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CharactersPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='charactersphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CharactersPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='eventsphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EventsPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='eventsphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EventsPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='institutionphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InstitutionPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='institutionphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InstitutionPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='miscellaneousphotocity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MiscellaneousPhotoCity', to='app.city'),
        ),
        migrations.AlterField(
            model_name='miscellaneousphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MiscellaneousPhotoVillage', to='app.village'),
        ),
        migrations.AlterField(
            model_name='panoramicphotovillage',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PanoramicPhotoVillage', to='app.village'),
        ),
    ]
