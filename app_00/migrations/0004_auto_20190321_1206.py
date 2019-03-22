# Generated by Django 2.1.7 on 2019-03-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_00', '0003_auto_20190314_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='app_00/photos', verbose_name='Photo'),
        ),
    ]
