# Generated by Django 4.0.2 on 2022-02-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateField()),
                ('collector_code', models.CharField(blank=True, max_length=30, null=True)),
                ('account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('cash_amount', models.FloatField(blank=True, null=True)),
                ('check_amount', models.FloatField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('check_number', models.CharField(blank=True, max_length=30, null=True)),
                ('or_no', models.CharField(blank=True, max_length=30, null=True)),
                ('teller_code', models.CharField(blank=True, max_length=30, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('payment_date', models.DateField()),
                ('biller', models.CharField(blank=True, max_length=30, null=True)),
                ('user_id', models.CharField(blank=True, max_length=30, null=True)),
                ('account_id', models.CharField(blank=True, max_length=30, null=True)),
                ('account_name', models.CharField(blank=True, max_length=30, null=True)),
                ('remarks', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
