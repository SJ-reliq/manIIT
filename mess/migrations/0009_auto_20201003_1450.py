# Generated by Django 3.1.1 on 2020-10-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0008_auto_20200930_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess_model',
            name='breakfast',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mess_model',
            name='breakfast2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mess_model',
            name='dinner',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mess_model',
            name='dinner2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mess_model',
            name='lunch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mess_model',
            name='lunch2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
