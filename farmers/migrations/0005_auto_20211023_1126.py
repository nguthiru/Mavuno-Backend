# Generated by Django 3.2.8 on 2021-10-23 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0004_bid_bid_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ('-date_made',)},
        ),
        migrations.AlterModelOptions(
            name='produce',
            options={'ordering': ('-date_added',)},
        ),
    ]