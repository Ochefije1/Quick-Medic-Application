# Generated by Django 4.2.1 on 2023-05-30 12:14

import app.models
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
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='media')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('speaciality', models.CharField(default=app.models.Specialization, max_length=255, null=True)),
                ('portfolio_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name of drugs')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Symptoms')),
            ],
        ),
        migrations.CreateModel(
            name='RequestConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symptoms', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='app.doctor', verbose_name='Request for consultation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illness', models.CharField(max_length=100)),
                ('drugs', models.TextField(verbose_name=app.models.Drugs)),
                ('allergies', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='Patients_attended', to='app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Medical_history', to='app.patient', verbose_name='Medical History')),
                ('symptoms', models.ManyToManyField(to='app.symptoms')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('virtual', 'virtual'), ('physical', 'physical'), ('private', 'private')], max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date and Time for appointment')),
                ('consult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.requestconsultation')),
            ],
        ),
    ]
