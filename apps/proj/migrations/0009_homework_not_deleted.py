# Generated by Django 4.0.3 on 2022-03-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0008_file_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='not_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
