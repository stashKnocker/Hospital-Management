# Generated by Django 2.1 on 2021-06-16 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=255)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50)),
                ('Age', models.PositiveIntegerField(null=True)),
                ('Date_of_birth', models.DateField(help_text='Please Enter the following in YYYY-MM-DD')),
                ('Aadhar_number', models.CharField(max_length=12, unique=True)),
                ('Marital_status', models.CharField(choices=[('Unmarried', 'Unmarried'), ('Married', 'Married'), ('Widow', 'Widow')], max_length=50)),
                ('Father_name', models.CharField(help_text='if not please enter husband or guardian name.', max_length=255)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('Address_1', models.CharField(max_length=900)),
                ('Address_2', models.CharField(blank=True, max_length=900, null=True)),
                ('City', models.CharField(max_length=100)),
                ('Zipcode', models.CharField(max_length=8)),
                ('Country', models.CharField(max_length=100)),
                ('Appointment_date', models.DateField(help_text='Please Enter the following in YYYY-MM-DD')),
                ('blood_group', models.CharField(choices=[('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=50)),
                ('Weight', models.FloatField(blank=True, null=True)),
                ('Height', models.FloatField(blank=True, null=True)),
                ('Blood_Sugar', models.FloatField(blank=True, null=True)),
                ('Blood_Pressure', models.FloatField(blank=True, null=True)),
                ('allergies', models.CharField(blank=True, max_length=900, null=True)),
                ('already_taken_tablet', models.CharField(max_length=900)),
                ('foods_taken_before_consulation', models.TextField()),
                ('department', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
