# Generated by Django 3.2.9 on 2021-11-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211127_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='about_adv',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='about_adv '),
        ),
        migrations.AlterField(
            model_name='adv',
            name='catalog_adv',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='catalog_adv'),
        ),
        migrations.AlterField(
            model_name='adv',
            name='contact_adv',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='contact_adv '),
        ),
        migrations.AlterField(
            model_name='adv',
            name='main_adv',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='main_adv'),
        ),
    ]
