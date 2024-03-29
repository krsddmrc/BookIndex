# Generated by Django 4.1.7 on 2023-03-13 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapi', '0002_phrase_page_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='phrase',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Phrase', to='indexapi.user'),
            preserve_default=False,
        ),
    ]
