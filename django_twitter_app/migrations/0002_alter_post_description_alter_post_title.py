# Generated by Django 4.1.3 on 2022-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, unique=True, verbose_name='Заголовок'),
        ),
    ]
