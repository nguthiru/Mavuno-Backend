# Generated by Django 3.2.8 on 2021-10-16 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='farmLogos'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='farmers.farm'),
        ),
        migrations.AlterField(
            model_name='produceimages',
            name='produce',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produce_images', to='farmers.produce'),
        ),
        migrations.DeleteModel(
            name='FarmLogos',
        ),
    ]
