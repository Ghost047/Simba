import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

class Role(models.Model):
	#member = models.OneToOneField(UserProfile)
	name = models.CharField(max_length=128)
	label = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Course, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to = '/static/images/avatars/', default = '/static/images/av_default.jpg')
	birthplace = models.CharField(max_length=128)
	provincia = models.CharField(max_length=10)
	birthdate = models.DateField(auto_now_add=False, default=0)	
	lives = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	course = models.ForeignKey(Course)
	is_fc = models.BooleanField(default=False)
	anno = models.CharField(max_length=128, default="primo")
	indirizzo = models.CharField(max_length=128, default="scienze delle merendine")
	matricola = models.CharField(max_length=128, default="0")
	role = models.ForeignKey(Role, default=1)
	status = models.BooleanField(default=False) #Modifica sta cosa sull'att di user
	wifi_pending = models.BooleanField(default=False)
	wifi_access = models.CharField(max_length=128, default="0")
	size = models.CharField(max_length=128, default="M")

	

	def __unicode__(self):
		return self.user.username

class Evento(models.Model):
	name = models.CharField(max_length=128)
	maino = models.ManyToManyField(User)
	date = models.DateField(auto_now_add=True)
	desc = models.CharField(max_length=500)

	def __unicode__(self):
		return self.name

class Task(models.Model):
	event = models.ForeignKey(Evento)
	target = models.OneToOneField(User, default=None, related_name='task_target')
	sender = models.OneToOneField(User, related_name='task_sender')
	name = models.CharField(max_length=128)
	deadline = models.DateField(auto_now_add=False, default=0)
	created = models.DateField(auto_now_add=True)
	desc = models.CharField(max_length=500)
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class BetaCode(models.Model):
	code = models.CharField(max_length=128)
	gen_date = models.DateField(auto_now_add=True)
	valid = models.BooleanField(default=True)
	email = models.CharField(max_length=128, default="0")

	def __unicode__(self):
		return self.code


	
	
