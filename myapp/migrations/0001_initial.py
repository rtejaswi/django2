# Generated by Django 3.0.7 on 2020-06-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=10)),
                ('student_usn', models.CharField(max_length=10)),
                ('student_phno', models.CharField(max_length=10)),
                ('student_avrage_marks', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=3)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student')),
            ],
        ),
    ]