# Generated by Django 3.1 on 2020-09-25 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200925_1524'),
        ('post', '0004_auto_20200925_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]