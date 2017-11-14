from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DetailView,TemplateView
def home(request):
    return render(request,'ecommerce/index.html')
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

#for adding subscribed user to database
from admin_interface.models import SubscribedUsers
from ecommerce.models import MyUser
from django.shortcuts import reverse
from .forms import AddSubscribedUserForm
from django.core.mail import send_mail,EmailMultiAlternatives
class AddSubscriptionUser(CreateView):
    template_name = 'ecommerce/index.html'
    form_class = AddSubscribedUserForm

    def get_success_url(self,form):
        return render(self.request, 'ecommerce/successful_register.html', {'message': 'Succesfully subscribed'})

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        already_exists = MyUser.objects.filter(email__exact=self.object.email)
        if already_exists:
            form.cleaned_data['email'] = ''
            return HttpResponseRedirect('/')
        else:
            already_subscribed = SubscribedUsers.objects.filter(email__exact=self.object.email)
            if already_subscribed:
                return HttpResponseRedirect('/')

            else:
                form.save()
                send_mail(
                'Successfully Subscribed',
                'Thank you for joining us',
                'dheeraja123456@gmail.com',
                [self.object.email],
                )

        return self.get_success_url(form)


from .models import Category,Product

class CategoryList(ListView):
    template_name = 'ecommerce/category.html'
    model = Category
    context_object_name = 'categories'


class Product_list_Category(ListView):
    template_name = 'ecommerce/productpage.html'
    model = Product

    def get_queryset(self):
        category = Category.objects.filter(id=self.kwargs['pk'])
        product_list_category_wise = Product.objects.filter(product_category=category)
        return product_list_category_wise