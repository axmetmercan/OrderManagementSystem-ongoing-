# Generated by Django 4.0.2 on 2022-03-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0009_alter_product_default_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='default_variant',
            field=models.CharField(default=1, max_length=100, verbose_name='Varsayılan Varyant Kodu'),
        ),
    ]
