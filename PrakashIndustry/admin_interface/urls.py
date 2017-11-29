from django.conf.urls import url
from .views import HomeAdmin
app_name = 'admin_interface'


urlpatterns = [
    url(r'^login$',HomeAdmin.as_view,name='home_admin')
]