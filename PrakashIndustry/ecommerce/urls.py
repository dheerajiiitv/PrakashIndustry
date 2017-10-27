from django.conf.urls import url
from .views import signup,afterLogin,Login,home,Logout
app_name = 'ecommerce'
urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^register/$',signup,name='register'),
    url(r'^timepass/$',afterLogin,name='timepass'),
    url(r'^login/$',Login.as_view(),name='login'),
    url(r'^logout/$',Logout.as_view(),name='logout')


]