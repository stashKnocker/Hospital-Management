# Generated by Django 2.1 on 2021-07-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescrip', '0007_auto_20210701_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='Age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='Fullname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='prescription',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='', max_length=50),
        ),
    ]
