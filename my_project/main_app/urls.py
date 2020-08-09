from django.conf.urls import url
from . import views

app_name = 'main_app'


urlpatterns = [

    url(r'^index/$',views.index,name='index'),
    url(r'^charts/$',views.charts,name='charts'),
    url(r'^cards/$',views.cards,name='cards'),
    url(r'^buttons/$',views.buttons,name='buttons'),
    url(r'^404/$',views.index,name='404'),
    url(r'^tables/$',views.tables,name='tables'),
    url(r'^utilities-animation/$',views.animation,name='utilities-animation'),
    url(r'^utilities-border/$',views.border,name='utilities-border'),
    url(r'^utilities-color/$',views.color,name='utilities-color'),
    url(r'^utilities-other/$',views.other,name='utilities-other'),
]