# Generated by Django 4.2.4 on 2023-08-03 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Add News', 'verbose_name_plural': 'Add News'},
        ),
    ]
