# Generated by Django 3.2.12 on 2023-04-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Payment pending', 'Payment pending'), ('Payment done', 'Payment done')], default='Payment pending', max_length=100),
        ),
    ]
