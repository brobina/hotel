from django.db import models

# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=100)
	post = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	def __str__(self):
		return self.name