from django.conf.urls import url
from .views import LinkCreateView, LinkUpdateView, LinkListView

urlpatterns = [
    url(r'^$', LinkListView.as_view(), name='list'),
    url(r'^new/$', LinkCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', LinkUpdateView.as_view(), name='update'),
]
