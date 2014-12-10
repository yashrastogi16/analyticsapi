from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
# user URLS
router.register(r'roles',rolesViewSet)
router.register(r'user',userViewSet)
router.register(r'organisation',organisationViewSet)
router.register(r'devices',devicesViewSet)
router.register(r'stores',storesViewSet)
router.register(r'rewards',rewardsViewSets)
router.register(r'membership',membershipViewSet)
router.register(r'stamptransaction',stamptransactionViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analyticsapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^analyticsapi/api/',include(router.urls)),
    url(r'^user/(?P<id>[0-9]+)$', 'api.views.userd', name='userd'),
    url(r'^stampdelivered/(?P<id>[a-zA-Z0-9]+)$', 'api.views.store', name='store'),
    url(r'^storeusers/(?P<id>[a-zA-Z0-9]+)$', 'api.views.usernum', name='usernum'),
    url(r'^redeemrewards/(?P<id>[a-zA-Z0-9]+)$', 'api.views.redeemreward', name='redeemreward'),
    url(r'^analytics/(?P<id>[a-zA-Z0-9]+)$','api.views.analytics',name='analytics')
    # url(r'^snippets/(?P<pk>[0-9]+)$', 'snippet_detail', name='snippet_detail'),
)
