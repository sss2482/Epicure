# Generated by Django 3.2.12 on 2023-04-17 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0005_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]