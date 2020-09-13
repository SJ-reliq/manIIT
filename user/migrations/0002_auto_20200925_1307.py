# Generated by Django 3.1 on 2020-09-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='role',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AddField(
            model_name='user',
            name='authoritystatus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]