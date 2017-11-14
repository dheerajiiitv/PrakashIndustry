from django.conf.urls import url
from .views import signup,afterLogin,Login,home,Logout,AddSubscriptionUser,CategoryList,Product_list_Category
app_name = 'ecommerce'
urlpatterns = [
    url(r'^$',AddSubscriptionUser.as_view(),name='home'),
    url(r'^register/$',signup,name='register'),
    url(r'^timepass/$',afterLogin,name='timepass'),
    url(r'^login/$',Login.as_view(),name='login'),
    url(r'^logout/$',Logout.as_view(),name='logout'),
    url(r'^subscribr/$',AddSubscriptionUser.as_view(),name='subscribe'),
    url(r'^categories/$',CategoryList.as_view(),name='category'),
    url(r'^productList/category(?P<pk>[0-9a-f-]+)$',Product_list_Category.as_view(),name='product_list')



]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)