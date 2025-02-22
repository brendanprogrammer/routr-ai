# Generated by Django 5.0.7 on 2025-02-18 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop1_comments',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop1_customer_address',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop1_customer_name',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop1_pallets_in',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop1_pallets_out',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop2_comments',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop2_customer_address',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop2_customer_name',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop2_pallets_in',
        ),
        migrations.RemoveField(
            model_name='drivertriprecord',
            name='stop2_pallets_out',
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=255, null=True)),
                ('pallets_in', models.IntegerField(blank=True, null=True)),
                ('pallets_out', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('trip_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='trip_records.drivertriprecord')),
            ],
        ),
    ]
