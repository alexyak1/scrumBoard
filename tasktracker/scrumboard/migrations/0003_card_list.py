# Generated by Django 3.0.6 on 2020-05-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20200527_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
            preserve_default=False,
        ),
    ]