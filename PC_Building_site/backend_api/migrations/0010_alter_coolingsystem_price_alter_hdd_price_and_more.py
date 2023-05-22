# Generated by Django 4.2.1 on 2023-05-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_powerunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coolingsystem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='hdd',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='powerunit',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='processor',
            name='frequency',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='processor',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ram',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='sdd',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
