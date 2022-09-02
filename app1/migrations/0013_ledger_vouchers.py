# Generated by Django 3.2.13 on 2022-09-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_companies_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger_vouchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('particulars', models.CharField(max_length=225)),
                ('account', models.CharField(max_length=225, null=True)),
                ('voucher_type', models.CharField(max_length=225, null=True)),
                ('voucher_no', models.CharField(max_length=225)),
                ('debit', models.CharField(max_length=225)),
                ('credit', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
            ],
        ),
    ]