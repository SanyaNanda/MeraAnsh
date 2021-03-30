from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)
	file = models.FileField()

	def get_absolute_url(self):
		return reverse('home')

class Prescriptions(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever_pres', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)

	def get_absolute_url(self):
		return reverse('home')

# class User(AbstractUser):
# 	is_parent = models.BooleanField(default=False, related_name='parent')
# 	is_doctor = models.BooleanField(default=False, related_name='doc')