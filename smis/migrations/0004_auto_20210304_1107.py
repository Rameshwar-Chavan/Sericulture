# Generated by Django 3.1.5 on 2021-03-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smis', '0003_auto_20210304_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form4',
            name='good_kosh_count',
        ),
        migrations.AddField(
            model_name='form4',
            name='good_kosh_kg',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='form4',
            name='good_kosh_rate',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='form4',
            name='Andipunj_count',
            field=models.FloatField(default=None),
        ),
    ]