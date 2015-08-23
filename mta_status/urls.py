from django.conf.urls import include, url
from django.contrib import admin
from status.views import StatusView

urlpatterns = [
    # Examples:
    # url(r'^$', 'mta_status.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', StatusView.as_view(), name='home'),
    url(r'^status/', include('status.urls')),
    url(r'^mta_auth/', include('mta_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
