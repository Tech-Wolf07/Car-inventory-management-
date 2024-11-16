# Generated by Django 4.2.16 on 2024-11-14 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=20)),
                ('colour', models.CharField(default=None, max_length=20)),
                ('no_of_owner', models.IntegerField(default=None)),
                ('kms_driven', models.IntegerField(default=None)),
                ('passing_till', models.DateField(default=None)),
                ('insuarance_till', models.DateField(default=None)),
                ('plate_no', models.CharField(default=None, unique=True)),
                ('status', models.CharField(choices=[('sale', 'For Sale'), ('buy', 'For Buy')])),
                ('year', models.DateField(default=None)),
                ('condition', models.TextField(default=None)),
                ('total_expenses', models.CharField(default=0)),
                ('profit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mob_no', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('p_type', models.CharField(choices=[('customer', 'Customer'), ('dealer', 'Dealer')], default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Expensens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('amount', models.BigIntegerField(default=0)),
                ('image_URL', models.ImageField(null=True, upload_to='')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobile.inventory')),
            ],
        ),
    ]
