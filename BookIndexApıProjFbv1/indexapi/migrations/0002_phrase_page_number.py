# Generated by Django 4.1.7 on 2023-03-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='page_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
