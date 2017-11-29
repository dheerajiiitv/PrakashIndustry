from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class MyUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')



        user = self.model(

            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,

        )

        user.set_password(password)
        user.save(using=self._db)
        user.is_admin = False
        return user

    def create_superuser(self,first_name,last_name, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(

            email,
            first_name,
            last_name,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=120,blank = False)
    last_name = models.CharField(max_length=120,blank = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.last_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Registration(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField(max_length=100)
    # sub_category = models.ManyToManyField('Category_under_Category')

    def __str__(self):
        return self.category_name





class Category_under_Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True,default=' ')


    def __str__(self):
        return self.category_name

from django.shortcuts import reverse
from django.db.models import  Q

class Product(models.Model):
    product_name = models.CharField("Product Name",max_length=100,unique=True)
    slug = models.SlugField(unique=True,max_length=100)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_category = models.ManyToManyField('Category',related_name='category')
    product_quantity = models.PositiveIntegerField()
    sub_category = models.ForeignKey(Category_under_Category, on_delete=models.CASCADE,related_name='sub_category')


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('ecommerce:product_detail', kwargs={'slug': self.slug})
    def get_product_total_rating(self):
        rating = CustomerReview.objects.filter(product=self)
        review_count = len(rating)
        return rating,review_count
    def get_product_rating(self):
        rating,review_count = self.get_product_total_rating()
        sum = 0
        for rvw in rating:
            sum +=rvw.rating
        if review_count is not 0:
            return sum/review_count
        else:
            return None

    def get_similar_product(self):
        sub_cat = []
        print(self.product_category.all().values_list('category_name'))
        for cat in self.product_category.all():
            sub_cat.append(cat.category_name)

        print(sub_cat)
        similar_product = Product.objects.filter(Q(product_category__category_name__in=sub_cat)
                                                 &Q(sub_category=self.sub_category)).all().distinct()

        return similar_product

FEATURED = (
    (0, 'Very bad'),
    (1, 'Bad'),
    (2, 'Normal'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent'),


)
from django.utils import timezone
class CustomerReview(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_reviewed')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_reviewed')
    review_date = models.DateField(default=timezone.now())
    rating = models.IntegerField(choices=FEATURED,default=0)
    review = models.TextField(blank=True)


    def __str__(self):
        return self.user.first_name + " " +self.user.last_name + " " + self.product.product_name

    def get_absolute_url(self):
        return reverse('products:product_review', kwargs={'pk': self.pk})


    class Meta:
        unique_together=('user','product')
def _image_upload(instance, filename):
    return f'products/{instance.product.slug}/{filename}'


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product')
    image = models.ImageField(upload_to=_image_upload)
    alt_text = models.CharField(max_length=20)


    def __str__(self):
        return self.product.product_name

class Address(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,blank=True,null=True)
    mobile_no = models.PositiveIntegerField()
    block_no = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50)
    area = models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin_code= models.PositiveIntegerField()
    to_deliver = models.BooleanField(default=True)




# class QuotedData(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     phone_number = models.PositiveIntegerField()
#     product_name = models.ManyToManyField('Product')
#     product_quantity=models.PositiveIntegerField(default=0)
#     date_of_delivery = models.DateField(default=timezone.now)
#     address = models.TextField()

class Orders(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)
    product_ordered = models.ForeignKey(Product)
    product_quantity = models.PositiveIntegerField()
    order_place_date = models.DateField(timezone.now())
    is_complete = models.BooleanField(default=False)


    def __str__(self):
       return self.product_ordered.product_name

