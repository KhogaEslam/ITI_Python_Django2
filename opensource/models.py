from __future__ import unicode_literals

from django.db import models

# Create your models here.


class track(models.Model):
	tr_name = models.CharField(max_length=200)

	def __str__(self):
		return self.tr_name


class student(models.Model):
	st_name = models.CharField(max_length=50)
	st_age = models.IntegerField()
	st_track = models.ForeignKey(track)

	def __str__(self):
		return self.st_name

	def is_born_before_1992(self):
		return self.st_age > 25
	is_born_before_1992.short_description = 'Check age'
	is_born_before_1992.boolean = True

