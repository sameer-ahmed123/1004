from django.db import models

class Employee(models.Model):
    eid = models.IntegerField(max_length=200)
    ename = models.CharField(max_length=200)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"
