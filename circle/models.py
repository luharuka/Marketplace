from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Article(models.Model):

	title = models.CharField(validators=[MinLengthValidator(1)], max_length=64, blank=False, null=False, default="Title")

	description = models.CharField(max_length=255, blank=True, null=False)

	image = models.ImageField(blank=True, null=False)

	price = models.FloatField(validators=[MinValueValidator(1)], blank=False, null=False, default=1)

	def __str__(self):
			return f"{self.name}"

	class Meta:
		db_table = 'article'
		verbose_name = 'circle_article'


class Person(models.Model):

	options = (('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say'))

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")

	username = models.CharField(max_length=64, blank=False, null=False, unique=True)
	bio = models.CharField(max_length=500, blank=True, null=False)

	first = models.CharField(max_length=64, blank=False, null=False)
	last = models.CharField(max_length=64, blank=True, null=False)

	age = models.IntegerField(blank=False, null=False)
	sex = models.CharField(max_length=1, choices=options, blank=False, null=False, default='X')

	email = models.EmailField(blank=False, null=False, unique=True)
	ph_no = models.BigIntegerField(blank=False, null=False, unique=True)

	rented = models.ManyToManyField(Article, blank=True, related_name="rented")
	bought = models.ManyToManyField(Article, blank=True, related_name="purchased")

	sold = models.ManyToManyField(Article, blank=True, related_name="sold")
	
	cart = models.ManyToManyField(Article, blank=True, related_name="cart")

	bookmarked = models.ManyToManyField(Article, blank=True, related_name="bookmarked")

	following = models.ManyToManyField('self', blank=True, related_name="following")

	allowsMessage = models.BooleanField(null=False, default=True)

	def __str__(self):
		return f"{self.first} {self.last}  {self.age}  {self.sex}"
	
	class Meta:
		db_table = "person"
		verbose_name = "circle_person"
		get_latest_by = "id"
		ordering = ['id']


class Message(models.Model):

	sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="send")

	receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receive")

	text = models.CharField(validators=[MinLengthValidator(1), MaxLengthValidator(255)], max_length=255, blank=False, null=False)

	timestamp = models.DateTimeField(blank=False, null=False, default=datetime.now)

	def __format__(self):
		return f"{self.sender} -> {self.receiver}"

	def __str__(self):
		return f"{self.timestamp}"


	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	#     if created:
	#         Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	#     instance.profile.save()
