# Generated by Django 3.1.5 on 2021-03-03 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smis', '0002_auto_20210224_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form4',
            name='Andipunj_count',
        ),
        migrations.RemoveField(
            model_name='form4',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='form4',
            name='चांगल्या_कोषांचे_वजन_कि_ग्रॅ',
        ),
        migrations.RemoveField(
            model_name='form4',
            name='चांगल्या_कोषांना_मिळालेला_दर_प्रति_कि_ग्रॅ',
        ),
    ]