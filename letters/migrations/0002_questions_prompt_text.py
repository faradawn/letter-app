# Generated by Django 3.1.7 on 2021-04-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='prompt_text',
            field=models.CharField(default='default prompt hey', max_length=200),
        ),
    ]
