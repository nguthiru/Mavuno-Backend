# Generated by Django 3.2.8 on 2021-10-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_auto_20211016_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_price',
            field=models.DecimalField(decimal_places=2, default=40.0, max_digits=16),
            preserve_default=False,
        ),
    ]
