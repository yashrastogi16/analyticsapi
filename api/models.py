from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

# Users of Stampitgo

class user(models.Model):
	_id = models.CharField(max_length=250)
	name = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=255)
	username = models.CharField(max_length=100, null = True)
	mobile = models.CharField(max_length=50,null = True)
	device = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	created_type = models.CharField(default = 'Stamp', max_length=100)
	def __unicode__(self):
		return smart_unicode(self.username)

# Roles of users

class roles(models.Model):
	code = models.CharField(max_length=50)
	name = models.CharField(max_length=150)
	def __unicode__(self):
		return smart_unicode(self.name)

# Organisations using Stampitgo

class organisation(models.Model):
	_id = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	description = models.TextField()
	code = models.CharField(max_length=100)
	def __unicode__(self):
		return smart_unicode(self.name)

# Devices used by the user

class devices(models.Model):
	did = models.CharField(max_length=250, default=0)
	user = models.CharField(max_length=250)
	platform = models.CharField(max_length=250)
	_id = models.CharField(max_length=250)
	_v = models.CharField(max_length=50)
	createdAt = models.DateTimeField()
	def __unicode__(self):
		return smart_unicode(self.user)

# Stores Using Stampitgo

class stores(models.Model):
	_id = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	active_card = models.CharField(max_length=100)
	add_city = models.CharField(max_length=100)
	add_address = models.TextField()
	admin = models.CharField(max_length=250)
	organization = models.CharField(max_length=250)
	created = models.DateTimeField()
	def __unicode__():
		return smart_unicode(self.name)

# Stampitgo Rewards

class rewards(models.Model):
	_id = models.CharField(max_length=250)
	user = models.CharField(max_length=250)
	stamp_card = models.CharField(max_length=250)
	store = models.CharField(max_length=250)
	redeem_status = models.CharField(max_length=250)
	created = models.DateTimeField()
	code = models.CharField(max_length=50)
	description = models.TextField()
	title = models.TextField()
	def __unicode__(self):
		return smart_unicode(self._id)

# Stampitgo Memberships

class membership(models.Model):
	_id = models.CharField(max_length=250)
	store = models.CharField(max_length=250)
	user = models.CharField(max_length=250)
	stamp_count = models.CharField(max_length=50)
	last_visit = models.DateTimeField()
	state = models.CharField(max_length=250)
	membership = models.CharField(max_length =225)
	def __unicode__(self):
		return smart_unicode(self._id)

# Stamp Transactions

class stamptransaction(models.Model):
	user = models.CharField(max_length=250)
	loyaltycards = models.CharField(max_length=250)
	store = models.CharField(max_length=250)
	_id = models.CharField(max_length=250)
	createdAt = models.DateTimeField()
	total = models.CharField(max_length=250)
	state = models.CharField(max_length=250)
	stamp_count = models.CharField(max_length=250)
	version = models.CharField(max_length=10)
	def __unicode__():
		return smart_unicode(self._id)
