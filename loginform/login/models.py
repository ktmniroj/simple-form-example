from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 200)
	phone_num = models.IntegerField()
	profile_picture = models.ImageField(upload_to = 'Image')

	def __str__(self):
		return 'name: {}'.format(self.name)

