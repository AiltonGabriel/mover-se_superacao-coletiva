# Generated by Django 4.1.1 on 2022-12-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_donation_collector_id_donation_id_checkout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='collector_id',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='is_payment_approved',
        ),
        migrations.AlterField(
            model_name='donation',
            name='id_checkout',
            field=models.CharField(default='', max_length=255, verbose_name='Id do pagamento (Mercado Pago)'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='payment_infos',
            field=models.JSONField(default=None, null=True, verbose_name='Informações do Pagamento (Mercado Pago)'),
        ),
    ]
