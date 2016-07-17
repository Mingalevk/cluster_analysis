from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, default='name')
    group_number = models.CharField(max_length=7)

    def __str__(self):
        return str(self.id)
# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Scores(models.Model):
    student = models.ForeignKey(Student)
    discipline = models.ForeignKey(Discipline)
    score = models.DecimalField(max_digits=3, decimal_places=2, default=2)

    def __str__(self):
        return str(self.score)
