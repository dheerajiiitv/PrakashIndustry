from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'ecommerce/home.html')
def signup(request):
    is_register = False;
    form1 = UserCreationForm(request.POST or None)
    if form1.is_valid():
        form_final = form1.save(commit=True)
        is_register = True;
        print(form1.cleaned_data['password1'])
        user = authenticate(email=form1.cleaned_data['email'],
                            password=form1.cleaned_data['password1'],
                            )

        login(request, user)
        return HttpResponseRedirect(reverse('ecommerce:home'))
    else:
        return render(request, 'ecommerce/signup.html', {'form1':form1,'is_register':is_register})


def afterLogin(request):
    return HttpResponse("Hello")

class Login(LoginView):
    template_name = 'ecommerce/login.html'

class Logout(LogoutView):
    next_page = reverse_lazy('ecommerce:home')
    # form_class = < class 'django.contrib.auth.forms.AuthenticationForm'>









