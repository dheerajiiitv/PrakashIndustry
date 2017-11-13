from django.conf.urls import url
from .views import signup,afterLogin,Login,home,Logout,AddSubscriptionUser
app_name = 'ecommerce'
urlpatterns = [
    url(r'^$',AddSubscriptionUser.as_view(),name='home'),
    url(r'^register/$',signup,name='register'),
    url(r'^timepass/$',afterLogin,name='timepass'),
    url(r'^login/$',Login.as_view(),name='login'),
    url(r'^logout/$',Logout.as_view(),name='logout'),
    url(r'^subscribr/$',AddSubscriptionUser.as_view(),name='subscribe')


]