# Generated by Django 3.1.4 on 2022-10-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackify_app', '0009_auto_20221021_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pressess',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]