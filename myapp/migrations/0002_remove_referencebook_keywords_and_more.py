# Generated by Django 4.2.17 on 2024-12-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencebook',
            name='keywords',
        ),
        migrations.AddField(
            model_name='keyword',
            name='reference_books',
            field=models.ManyToManyField(related_name='keywords', to='myapp.referencebook', verbose_name='Associated Reference Books'),
        ),
    ]
