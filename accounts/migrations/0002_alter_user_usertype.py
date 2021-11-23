# Generated by Django 3.2.8 on 2021-11-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('F', 'Farmer'), ('N', 'Normal'), ('A', 'Agrovet'), ('P', 'Professional'), ('B', 'Business')], max_length=2),
        ),
    ]
