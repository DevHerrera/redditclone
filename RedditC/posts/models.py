from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	tittle = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	pub_date = models.DateField()
	author = models.ForeignKey(User, default="")
	votes_total = models.IntegerField(default=1)

	def __str__(self):
		return self.tittle
