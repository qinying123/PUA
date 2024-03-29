# Generated by Django 2.2.3 on 2019-08-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pua_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
