# Generated by Django 3.1.4 on 2022-10-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackify_app', '0010_auto_20221021_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]