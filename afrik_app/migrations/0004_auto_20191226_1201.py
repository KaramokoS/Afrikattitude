# Generated by Django 2.2.1 on 2019-12-26 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afrik_app', '0003_auto_20191226_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='body',
            new_name='Message',
        ),
    ]