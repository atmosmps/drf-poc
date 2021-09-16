# Generated by Django 3.2.7 on 2021-09-16 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_alter_address_updated_at'),
        ('core', '0004_touristplace_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristplace',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]