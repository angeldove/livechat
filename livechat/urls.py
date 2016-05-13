"""livechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User

import chat.views as chat_views
import reg.views as reg_views

from rest_framework import routers, serializers, viewsets


# serializers define the api representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# routers provide an easy way of automatically determining the url conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', chat_views.home, name='home'),

    # auth URL confs
    url(r'^login/$', chat_views.login_page, name='login_page'),
    url(r'^logout/$', chat_views.logout_page, name='logout_page'),
    url(r'^accounts/logout/$', chat_views.logout_page, name='logout_page'),
    url(r'^accounts/login/$', chat_views.login_page, name='login_page'),

    # 'reg.views.reg_form' view
    url(r'register/$', reg_views.regform, name='regform'),

    # django rest framework urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^rooms/$', chat_views.room_list),
]
