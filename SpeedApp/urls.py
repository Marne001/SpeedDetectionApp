from django.conf.urls import url
from . import views

app_name = 'SpeedApp'

urlpatterns = [
    url(r'detect/$',views.DetectPageView.as_view(), name='detect'),
    url(r'calculate/(?P<pk>\d+)/$',views.SpeedDetailView.as_view(), name='speed-detail'),
]