from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    year_of_study = models.IntegerField(null=False)

    def __str__(self):
        return 'ID: {},Name:{}'.format(self.id, self.name)