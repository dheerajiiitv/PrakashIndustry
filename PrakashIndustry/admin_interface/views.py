from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,CreateView
# from ecommerce.models import PromotionMessage
from django.contrib import  admin

class HomeAdmin(TemplateView):
    template_name = 'admin_home.html'

# @admin.register(PromotionMessage)
# class PromotionMessageAdmin(admin.ModelAdmin):
#     pass








