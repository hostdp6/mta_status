from django.conf.urls import url
from status.views import StatusView, FavoriteView

from . import views

urlpatterns = [
    url(r'^$', StatusView.as_view(), name='home'),
    url(r'^([A-Za-z]*)$', StatusView.as_view()),
    url(r'favorite/$', FavoriteView.as_view()),
]