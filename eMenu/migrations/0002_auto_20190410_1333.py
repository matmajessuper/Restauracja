# Generated by Django 2.2 on 2019-04-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eMenu.Card'),
        ),
    ]
