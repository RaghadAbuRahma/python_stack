# Generated by Django 2.2.4 on 2024-05-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20240521_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='massages',
            name='massage',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]