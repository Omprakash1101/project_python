# Generated by Django 4.1.7 on 2023-02-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
