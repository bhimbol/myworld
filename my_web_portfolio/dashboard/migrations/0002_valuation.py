# Generated by Django 4.0.6 on 2023-12-07 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.TextField()),
                ('description', models.TextField()),
                ('cs', models.IntegerField()),
                ('ib', models.IntegerField()),
                ('pcs', models.IntegerField()),
            ],
        ),
    ]
