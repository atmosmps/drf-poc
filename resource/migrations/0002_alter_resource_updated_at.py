# Generated by Django 3.2.7 on 2021-09-16 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]