# Generated by Django 4.1.7 on 2023-03-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='offer',
        ),
        migrations.AddField(
            model_name='price',
            name='offer_1',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer1'),
        ),
        migrations.AddField(
            model_name='price',
            name='offer_2',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer2'),
        ),
        migrations.AddField(
            model_name='price',
            name='offer_3',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer3'),
        ),
        migrations.AddField(
            model_name='price',
            name='offer_4',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer4'),
        ),
        migrations.AddField(
            model_name='price',
            name='offer_5',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer5'),
        ),
        migrations.AddField(
            model_name='price',
            name='offer_6',
            field=models.TextField(default='0000000', editable=False, verbose_name='Offer6'),
        ),
        migrations.AddField(
            model_name='price',
            name='plan_name',
            field=models.CharField(default='0000000', editable=False, max_length=50, verbose_name='Plan'),
        ),
    ]
