# Generated by Django 2.2 on 2019-04-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0003_auto_20190410_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='dish',
        ),
        migrations.AddField(
            model_name='card',
            name='dish',
            field=models.ManyToManyField(null=True, to='eMenu.Dish'),
        ),
    ]