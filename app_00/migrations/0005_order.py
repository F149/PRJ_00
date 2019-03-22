# Generated by Django 2.1.7 on 2019-03-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_00', '0004_auto_20190321_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Client name')),
                ('phone', models.CharField(max_length=30, verbose_name='Client phone')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_00.Book', verbose_name='Book title')),
            ],
        ),
    ]