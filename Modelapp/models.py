from django.db import models


class Students(models.Model):
    Student_ID = models.IntegerField(default=0, primary_key=True)
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    EmailAddress = models.EmailField(max_length=30)
    Date_of_Birth = models.DateField()
    Age = models.IntegerField()

    class Meta:
        db_table = 'Wanafunzi'


class Teachers(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    EmailAddress = models.EmailField(max_length=30)

    def __str__(self):
        return self.Firstname


class Parents(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    EmailAddress = models.EmailField(max_length=30)
    Phone_No = models.IntegerField()
    ID_No = models.IntegerField()

    def __str__(self):
        return self.Firstname


class Courses(models.Model):
    CourseName = models.CharField(max_length=20)
    CourseID = models.IntegerField()
    Grade = models.IntegerField()
    Student_ID = models.IntegerField(default=0, primary_key=True)

    def __str__(self):
        return self.CourseName


class Posts(models.Model):
    Title = models.CharField(max_length=20)
    Author = models.CharField(max_length=20)
    Date_Updated = models.DateField()

    def __str__(self):
        return self.Title


