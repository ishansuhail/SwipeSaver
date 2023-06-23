from django.db import models


# Create your models here.


class Survey(models.Model):
	
	question1 = models.CharField('question 1', max_length=1024)
	question2 = models.CharField('question 2', max_length=1024)
	question3 = models.CharField('question 3', max_length=1024)
	question4 = models.CharField('question 4', max_length=1024)
	question5 = models.CharField('question 5', max_length=1024)

class contactForm(models.Model):
	email = models.EmailField('Email Address')
	name  = models.CharField('Name', max_length=64)
	title = models.CharField('Topic', max_length=256)
	description = models.TextField(blank=True)
	survey = models.ForeignKey(Survey,blank=True,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name







