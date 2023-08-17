from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    dept_loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class EMP(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    e_name=models.CharField(max_length=100)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)
    comm=models.IntegerField(null=True)
    hire_date=models.DateField()
    sal=models.IntegerField(default=10000)

    def __str__(self):
        return self.e_name

