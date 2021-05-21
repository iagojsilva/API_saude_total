# Generated by Django 3.1.5 on 2021-04-03 18:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210402_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('D01', '13-4-2021'), ('D02', '14-4-2021'), ('D03', '15-4-2021'), ('D04', '16-4-2021'), ('D05', '17-4-2021'), ('D06', '18-4-2021'), ('D07', '19-4-2021')], default=('D01', '13-4-2021'), max_length=23),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='horario_disponiveis',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('T01', '13:30'), ('M01', '09:30'), ('T02', '17:00'), ('T03', '19:00'), ('M02', '10:30'), ('M03', '07:00')], default=('T01', '13:30'), max_length=10),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='data_disponiveis',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('D01', '13-4-2021'), ('D02', '14-4-2021'), ('D03', '15-4-2021'), ('D04', '16-4-2021'), ('D05', '17-4-2021'), ('D06', '18-4-2021'), ('D07', '19-4-2021')], default=('D01', '13-4-2021'), max_length=23),
        ),
    ]