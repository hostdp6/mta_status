from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'login$', 'django.contrib.auth.views.login', {'redirect_field_name': '/status/'}),
    url(r'login/$', 'django.contrib.auth.views.login', {'redirect_field_name': '/status/'}),
    url(r'logout$', 'django.contrib.auth.views.logout', {'next_page': '/status/'}),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': '/status/'}),
]