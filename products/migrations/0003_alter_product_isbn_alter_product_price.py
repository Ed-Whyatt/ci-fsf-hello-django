# Generated by Django 4.1.2 on 2022-11-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=254),
        ),
    ]
