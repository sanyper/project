from django.db import models

# Create your models her



class Course(models.Model):
    idsubject = models.CharField(max_length=5)
    subject = models.CharField(max_length=64)
    term = models.PositiveIntegerField()
    year = models.CharField(max_length=4)
    seat = models.PositiveIntegerField(default = 3)
    status = models.BooleanField(default=True)

    def seatCheck(self):
        totalStd = self.subjects.all().count()
        if self.seat > totalStd:
            return self.status == True
        else:
            return self.status == False

    def statusCheck(self):
        status_info = self.seatCheck()
        if status_info == True:
            return "Available"
        else:
            return "Closed"

    def seatLeft(self):
        seat = self.seat
        taken = self.students.count()
        left = seat - taken
        return str(left)


class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    idstudent = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.first} {self.last} {self.idstudent}"
