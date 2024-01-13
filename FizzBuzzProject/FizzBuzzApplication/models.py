from django.db import models

class Parameter(models.Model):
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    str1 = models.CharField(max_length=200)
    str2 = models.CharField(max_length=200)
    hits = models.IntegerField(default=1)


