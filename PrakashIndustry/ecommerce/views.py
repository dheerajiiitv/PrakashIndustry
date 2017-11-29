from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DetailView,TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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


from .models import Category,Product,CustomerReview
from django.db.models import Avg
class CategoryList(ListView):
    template_name = 'ecommerce/category.html'
    model = Category
    context_object_name = 'categories'

from itertools import cycle
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
class Product_list_Category(ListView):
    template_name = 'ecommerce/productpage.html'
    model = Product
    paginate_by = 9
    category_name = ""
    def get_queryset(self):
        category = Category.objects.filter(id=self.kwargs['pk'])
        self.category_name = category
        print(self.category_name)
        product_list_category_wise = Product.objects.filter(product_category=category)
        # zipped = zip(cycle(self.get_avg_product_rating()),self.object_list)
        return product_list_category_wise




    def get_context_data(self, *args, **kwargs):
        context = super(Product_list_Category,self).get_context_data(**kwargs)
        context['category'] = self.category_name

        return context


class ProductDetails(DetailView):
    model = Product


from django.utils import timezone
@login_required()
def review(request,*args,**kwargs):
    if request.method == 'POST':
        review_text = request.POST['msg']
        rating = request.POST['rating']
        product = Product.objects.get(id=kwargs['pk'])
        try:
            customer_review = CustomerReview.objects.create(
                rating = rating,
                user = request.user,
                review = review_text,
                review_date = timezone.now(),
                product = product,
            )
            print(customer_review.product)
            print(customer_review.rating)
            print(customer_review.review_date)

            customer_review.save()
        except:
            return HttpResponseRedirect(reverse('ecommerce:product_detail',kwargs={'slug':product.slug}))


        return HttpResponseRedirect(reverse('ecommerce:product_detail',kwargs={'slug':product.slug}))

# from .models import QuotedData

# def get_quoted(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         phone_number = request.POST['phone_number']
#         date_of_delivery = request.POST['date']
#         addreess = request.POST['address']
#         try:
#             quoted = QuotedData.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 email = email,
#                 phone_number = phone_number,
#                 date_of_delivery = date_of_delivery,
#                 addreess =addreess
#             )
#
#             quoted.save(commit=False)
#
#         except:
#             return HttpResponseRedirect()


from carton.cart import Cart
@login_required()
def add(request,*args,**kwargs):
    cart = Cart(request.session)
    product = Product.objects.get(id=kwargs['pk'])
    slug = product.slug
    cart.add(product,price=product.product_price)

    return HttpResponseRedirect(reverse('ecommerce:product_detail',kwargs={'slug':slug}))


@login_required()
def remove(request,*args,**kwargs):
    cart = Cart(request.session)
    product = Product.objects.get(id=kwargs['pk'])
    cart.remove(product)
    return render(request,'ecommerce/show-cart.html',{'message':'Product removed succesfully'})


@login_required()
def show(request):
    return render(request,'ecommerce/show-cart.html')


@login_required()
def direct_order(request,*args,**kwargs):
    cart = Cart(request.session)
    product = Product.objects.get(id=kwargs['pk'])
    cart.add(product, price=product.product_price)
    return HttpResponseRedirect('/addAddress')

@login_required()
def change_quantity(request,*args,**kwargs):
    cart = Cart(request.session)
    product = Product.objects.get(id=kwargs['pk'])

    if request.method == "POST":
        quantiy =  int(request.POST['remove_quantity'])
        if quantiy > 0 and quantiy < product.product_quantity:
            cart.set_quantity(product,quantiy)
            return render(request,'ecommerce/show-cart.html',{'message':'Quantity changed succesfully'})
        else:
            return render(request,'ecommerce/show-cart.html',{'message':'Please Enter Valid quantity'})


    else:
        return render(request,'ecommerce/show-cart.html')
from .models import Address
from .forms import AddAddressForm
from random import randint
from twilio.rest import Client
class AddAddress(CreateView):
    form_class =AddAddressForm

    template_name = 'ecommerce/addAddress.html'

    success_url = '/entercode'

    def send_sms_verification(self):
        number = randint(100000,999999)
        account_sid = 'AC062178d3463fafaf0a8b544ae9601c19'
        auth_token = 'b433c64321419877897401b57a6a5632'
        client = Client(account_sid, auth_token)
        client.messages.create(from_='+12568278181', to=["+919408595308"], body=number)
        send_mail(
            'Successfully Subscribed',
            str(number),
            'dheeraja123456@gmail.com',
            [self.request.user.email],
        )

        return number

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.user = get_object_or_404(MyUser,email=self.request.user)
        code = self.send_sms_verification()
        self.request.session['cody'] = code
        try:
            self.object.save()
        except:
            return render(self.request,'ecommerce/addAddress.html',{'message':'already exist','form':form})

        return HttpResponseRedirect(self.get_success_url())
from .models import Orders
@login_required()
def codeView(request):
    return render(request,'ecommerce/entercode.html')

@login_required()
def checkCode(request):

    if request.method == 'POST':

        code_enter = int(request.POST['code'])
        code = request.session['cody']
        if code_enter == code:
            # for product_ordered in
            product_added_to_cart = Cart(request.session)
            print(request.user.email)
            for product,i in zip(product_added_to_cart.items,product_added_to_cart.products):
                order = Orders.objects.create(
                    user = request.user,
                    address = Address.objects.first(),
                    product_ordered = get_object_or_404(Product,id=i.id),
                    product_quantity = product.quantity,
                    order_place_date = timezone.now(),
                    is_complete = True,
                )
                order.save()
                product_quantity_change=get_object_or_404(Product,id=i.id)
                product_quantity_change.product_quantity = product_quantity_change.product_quantity - product.quantity
                product_quantity_change.save()
                product_added_to_cart.remove(product)

            account_sid = 'AC062178d3463fafaf0a8b544ae9601c19'
            auth_token = 'b433c64321419877897401b57a6a5632'
            client = Client(account_sid, auth_token)
            client.messages.create(from_='+12568278181', to=["+919408595308"], body="Your Order has been placed")
            send_mail(
                'Successfully Subscribed',
                'Thank you Your order has been placed.',
                'dheeraja123456@gmail.com',
                [request.user.email],
            )
            return render(request,'ecommerce/placeyourorder.html',{'message':'Order Placed Successfully'})

        else:
            return render(request,'ecommerce/entercode.html',{'message':'Wrong code'})


from django.shortcuts import get_list_or_404
class MyOrder(ListView):
    model = Orders
    template_name = 'ecommerce/myorders.html'

    def get_queryset(self):
        order =  get_list_or_404(Orders,user=self.request.user)
        return order

    def get_context_data(self, *args, **kwargs):
        context = super(MyOrder, self).get_context_data(**kwargs)
        context['orders_lists'] = self.get_queryset()

        return context


# from django.contrib.auth.views import password_reset
# def password_reset(request, is_admin_site=False,
#             template_name='registration/password_reset_form.html',
#             email_template_name='registration/password_reset_email.html',
#             password_reset_form=PasswordResetForm,
#             token_generator=default_token_generator,
#             post_reset_redirect=None):
#             pass

class GetQuoted(TemplateView):
    template_name = 'ecommerce/get_quoted.html'