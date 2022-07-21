# Generated by Django 4.0.5 on 2022-07-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,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', max_length=500),
        ),
    ]
