from django.db import models

class students(models.Model):
    student_name= models.CharField(max_length=200)
    student_roll=models.IntegerField(max_length=200)
    student_class=models.IntegerField(max_length=20)

    class Meta:
        db_table="student_details"