# Generated by Django 3.2.6 on 2021-10-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20211016_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_price',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]