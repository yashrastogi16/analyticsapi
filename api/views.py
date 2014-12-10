from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# User ViewSets

class userViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all()
	serializer_class = userSerializer

# User roles ViewSets
class rolesViewSet(viewsets.ModelViewSet):
	queryset = roles.objects.all()
	serializer_class = rolesSerializer

# Organisation ViewSets
class organisationViewSet(viewsets.ModelViewSet):
	queryset = organisation.objects.all()
	serializer_class = organisationSerializer

# Devices ViewSets

class devicesViewSet(viewsets.ModelViewSet):
	queryset = devices.objects.all()
	serializer_class = devicesSerializer
# Stores ViewSets

class storesViewSet(viewsets.ModelViewSet):
	queryset = stores.objects.all()
	serializer_class = storesSerializer

# Rewards ViewSets

class rewardsViewSets(viewsets.ModelViewSet):
	queryset = rewards.objects.all()
	serializer_class = rewardsSerializers

# Membership ViewSets

class membershipViewSet(viewsets.ModelViewSet):
	queryset = membership.objects.all()
	serializer_class = membershipSerializer

# StampTransactions ViewSets

class stamptransactionViewSet(viewsets.ModelViewSet):
	queryset = stamptransaction.objects.all()
	serializer_class = stamptransactionSerializer

@api_view(['GET', 'POST'])
def userd(request, id):
	try:
		user1 = user.objects.get(id = id)
		print user1
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		print "i am in get again"
		serializer = userSerializer(user1)
		return Response(serializer.data)


# Total Number of stamp Delivered

@api_view(['GET', 'POST'])
def store(request, id):
	try:
		strmp = stamptransaction.objects.filter(store = id)
	except strmp.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	count = 0
	if request.method == 'GET':
		tcount = {}
		serializer = stamptransactionSerializer(strmp, many=True)
		for i in serializer.data:
			count += 1
			print count,i
		serializer.data.append(count)
		tcount['count'] = count
		return Response(tcount)

# Total number of User of Particular Store

@api_view(['GET', 'POST'])
def usernum(request, id):
	try:
		usernum = membership.objects.filter(store = id)
	except usernum.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	count = 0
	if request.method == 'GET':
		tcount = {}
		serializer = membershipSerializer(usernum, many=True)
		for i in serializer.data:
			count += 1
			print count,i
		serializer.data.append(count)
		tcount['count'] = count
		return Response(tcount)

# Total number of stamps Redeemed

@api_view(['GET', 'POST'])
def redeemreward(request, id):
	try:
		redeem = rewards.objects.filter(store = id, redeem_status = 'true')
	except redeem.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	count = 0
	if request.method == 'GET':
		tcount = {}
		serializer = rewardsSerializers(redeem, many=True)
		for i in serializer.data:
			count += 1
			print count,i
		# serializer.data.append(count)
		tcount['count'] = count
		return Response(tcount)

@api_view(['GET', 'POST'])
def analytics(request, id):
	try:
		strmp = stamptransaction.objects.filter(store = id)
		usernum = membership.objects.filter(store = id)
		redeem = rewards.objects.filter(store = id, redeem_status = 'true')
	except redeem.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		stamp_count = 0
		redeem_count = 0
		user_count = 0
		tcount = {}
		data = {}
		serializer1 = stamptransactionSerializer(strmp, many=True)
		serializer2 = membershipSerializer(usernum, many=True)
		serializer3 = rewardsSerializers(redeem, many=True)
		for i in serializer1.data:
			stamp_count += 1
		for i in serializer2.data:
			user_count += 1
		for i in serializer3.data:
			redeem_count += 1
		if strmp and usernum and redeem:
			data['stamp_count'] = stamp_count
			data['user_count'] = user_count
			data['redeem_count'] = redeem_count
			tcount['data'] = data
			tcount['code'] = 1
			tcount.update(tcount)
			print type(tcount)
			print tcount
		else:
			data['msg'] = 'Invalid Store'
			tcount['data'] = data
			tcount['code'] = 0
		return Response(tcount)

