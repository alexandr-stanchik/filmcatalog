# Generated by Django 4.0.6 on 2022-07-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_filminstance_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filminstance',
            name='mark',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, max_length=2),
        ),
    ]
