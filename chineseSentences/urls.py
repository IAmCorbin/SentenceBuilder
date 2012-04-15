from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chineseSentences.views.home', name='home'),
    
    url(r'^accounts/login/$', 'chineseSentences.views.userlogin', name='userlogin'),
    url(r'^accounts/logout/$', 'chineseSentences.views.userlogout', name='userlogout'),
    url(r'^accounts/register/$', 'chineseSentences.views.register', name='register'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
