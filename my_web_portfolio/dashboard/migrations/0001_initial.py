# Generated by Django 4.0.6 on 2023-11-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.TextField()),
                ('description', models.TextField()),
                ('qtyperpcs', models.IntegerField()),
                ('bccs', models.TextField()),
                ('bcib', models.TextField()),
                ('bcpcs', models.TextField()),
            ],
        ),
    ]
