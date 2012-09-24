from django.conf.urls import patterns, include, url

urlpatterns += patterns('usersAuth.views',
    url(r'^login/$', 'loginUser', name='login'),
    url(r'^logout/$', 'logoutUser', name='logout'),
    url(r'^register/$', 'usersRegister', name='register'),
)


