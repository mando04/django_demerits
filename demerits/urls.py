from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'board.views.index', name='home'),
    url(r'^login/$', 'usersAuth.views.loginUser', name='login'),
    url(r'^logout/$', 'usersAuth.views.logoutUser', name='logout'),
    url(r'^addDemerit/$', 'board.views.updateDemerit', name='add'),
    url(r'^adduser$', 'board.views.addUser', name='adduser'),
    url(r'^register/$', 'usersAuth.views.usersRegister', name='register'),
 
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

