from django.db import models
from django.contrib.auth.models import User

class LineType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Line(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    text = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(LineType, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User)
    line = models.ForeignKey(Line)

    def __unicode__(self):
        return str(self.user) + '->' + str(self.line)
