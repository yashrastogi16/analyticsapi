from django.forms import widgets
from rest_framework import serializers
from models import *

#User Serializer

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('_id','name','email','username','mobile','device','code','role','created_at','created_type')

# Role of Users Serializer

class rolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = roles
		fields = ('code','name')

# Organisation Serializer

class organisationSerializer(serializers.ModelSerializer):
	class Meta:
		model = organisation
		fields = ('_id','name','description','code')

# Devices Serializer

class devicesSerializer(serializers.ModelSerializer):
	class Meta:
		model = devices
		fields = ('did','user','platform','_id','_v')

# Stores Serializer

class storesSerializer(serializers.ModelSerializer):
	class Meta:
		model = stores
		fields = ('_id','name','active_card','add_city','add_address','admin','organization','created')

# Rewards Serializer

class rewardsSerializers(serializers.ModelSerializer):
	class Meta:
		model = rewards
		fields = ('_id','user','stamp_card','store','redeem_status','created','code','description','title')

# Membership Serializer

class membershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = membership
		fields = ('_id','store','user','stamp_count','last_visit','state','membership')

# StampTransactions Serializer

class stamptransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = stamptransaction
		fields = ('user','loyaltycards','store','_id','createdAt','total','state','stamp_count','version')
