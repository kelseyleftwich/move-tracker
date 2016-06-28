"""move_tracker URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from packing import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	# object detail
	url(r'^boxes/(?P<box_id>[0-9]+)/$', views.box_detail, name='box_detail'),
	url(r'^things/(?P<thing_id>[0-9]+)/$', views.thing_detail, name='thing_detail'),
	# object edit
	url(r'^boxes/(?P<box_id>[-\w]+)/edit/$', views.edit_box, name='edit_box'),
	url(r'^things/(?P<thing_id>[-\w]+)/edit/$', views.edit_thing, name='edit_thing'),
	# browse
	url(r'^browse/things/name/$', views.browse_things_by_name, name='browse_things'),
	url(r'^browse/things/name/(?P<initial>[-\w]+)/$', views.browse_things_by_name, name='browse_things_by_name'),
	# admin
    url(r'^admin/', admin.site.urls),
]
