# Generated by Django 4.1.7 on 2023-03-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_name', models.CharField(max_length=30)),
                ('text_number', models.IntegerField()),
                ('phrase_number', models.IntegerField()),
                ('phrase_content', models.CharField(max_length=30)),
            ],
        ),
    ]
