from django.conf.urls import url
from .views import ShortURLRedirectView

urlpatterns = [
    url(r'^(?P<slug>\w{1,5})/$', ShortURLRedirectView.as_view(), name='redirect'),
]
