# Generated by Django 3.1.5 on 2021-04-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210403_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidade',
            name='nome',
            field=models.CharField(max_length=20),
        ),
    ]