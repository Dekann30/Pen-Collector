# Generated by Django 4.0.6 on 2022-07-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen_app', '0005_label_explaination'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='labels',
            field=models.ManyToManyField(to='pen_app.label'),
        ),
    ]
