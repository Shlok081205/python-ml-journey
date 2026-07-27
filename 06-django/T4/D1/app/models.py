from django.db import models

class Database(models.Model):

  enr = models.IntegerField()
  cl = models.IntegerField()
  name = models.TextField()

  def __str__(self):
      return str(self.enr)
  
