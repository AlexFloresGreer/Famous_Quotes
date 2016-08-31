from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
   url(r'^quotes', views.quotes),
   url(r'^addquote$', views.addquote),
   url(r'^addtofav/(?P<id>\d+)$', views.addtofav),
   url(r'^removefromfav/(?P<id>\d+)$', views.removefromfav),
   url(r'^users/(?P<id>\d+)$', views.quotecount),

  # url(r'^login$', views.login),
  # url(r'^success/(?P<name>\w+)$', views.success)
]
