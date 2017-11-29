from django.conf.urls import url
from .views import signup,afterLogin,Login,home,Logout,AddSubscriptionUser,CategoryList,\
                    Product_list_Category,ProductDetails,review,add,show,remove,change_quantity,checkCode,AddAddress,\
                        codeView,direct_order,GetQuoted,MyOrder
app_name = 'ecommerce'
urlpatterns = [
    url(r'^$',AddSubscriptionUser.as_view(),name='home'),
    url(r'^register/$',signup,name='register'),
    url(r'^timepass/$',afterLogin,name='timepass'),
    url(r'^login/$',Login.as_view(),name='login'),
    url(r'^logout/$',Logout.as_view(),name='logout'),
    url(r'^subscribr/$',AddSubscriptionUser.as_view(),name='subscribe'),
    url(r'^categories/$',CategoryList.as_view(),name='category'),
    url(r'^productList/category(?P<pk>[0-9a-f-]+)$',Product_list_Category.as_view(),name='product_list'),
    url(r'^productdetail(?P<slug>[\w-]+)$',ProductDetails.as_view(),name='product_detail'),
    url(r'^postreview(?P<pk>[\w-]+)$',review,name="product_review"),
    url(r'^add/(?P<pk>[\w-]+)$',add, name='shopping-cart-add'),
    url(r'^directorder/(?P<pk>[\w-]+)$',direct_order, name='direct_order'),
    url(r'^remove/(?P<pk>[\w-]+)$',remove, name='shopping-cart-remove'),
    url(r'^show/$',show, name='shopping-cart-show'),
    url(r'^changeQuantity/(?P<pk>[\w-]+)$',change_quantity, name='shopping-cart-change-quantity'),
    url(r'^addAddress/$',AddAddress.as_view(), name='add_address'),
    url(r'^entercode/$',codeView, name='enter_code'),
    url(r'^placeorder/$',checkCode, name='place_order'),
    url(r'^getquoted/$',GetQuoted.as_view(),name='get-quoted'),
    url(r'^myorders/$',MyOrder.as_view(),name='my_order')

]
from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)