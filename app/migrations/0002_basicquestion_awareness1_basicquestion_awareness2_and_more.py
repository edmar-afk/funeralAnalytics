# Generated by Django 5.0.6 on 2024-11-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicquestion',
            name='awareness1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicquestion',
            name='awareness2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicquestion',
            name='awareness3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicquestion',
            name='financial1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicquestion',
            name='financial2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]