# Generated by Django 2.2 on 2019-04-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0005_auto_20190410_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date_added',
            field=models.DateField(auto_now_add=True, verbose_name='Date added'),
        ),
        migrations.AlterField(
            model_name='card',
            name='date_updated',
            field=models.DateField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='date_added',
            field=models.DateField(auto_now_add=True, verbose_name='Date added'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='date_updated',
            field=models.DateField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='preparation_time',
            field=models.CharField(max_length=15, verbose_name='Preparation time'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='vegetarian',
            field=models.BooleanField(verbose_name='Vegetarian dish'),
        ),
    ]