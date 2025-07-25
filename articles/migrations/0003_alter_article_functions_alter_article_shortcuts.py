# Generated by Django 5.2.4 on 2025-07-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_function_title_shortcut_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='functions',
            field=models.ManyToManyField(blank=True, to='articles.function'),
        ),
        migrations.AlterField(
            model_name='article',
            name='shortcuts',
            field=models.ManyToManyField(blank=True, to='articles.shortcut'),
        ),
    ]
