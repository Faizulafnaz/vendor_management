# Generated by Django 4.2.7 on 2023-11-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_remove_vendor_vendor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]