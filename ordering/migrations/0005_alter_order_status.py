# Generated by Django 3.2.12 on 2023-04-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_auto_20230416_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Payment verification pending', 'Payment verification pending'), ('Payment verification done', 'Payment verification done')], default='Payment verification pending', max_length=100),
        ),
    ]