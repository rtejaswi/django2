from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length = 10)
    student_usn = models.CharField(max_length = 10)
    student_phno = models.CharField(max_length = 10)
    student_avrage_marks = models.DecimalField(max_digits=5, decimal_places=3)

class Hostel(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=3)
