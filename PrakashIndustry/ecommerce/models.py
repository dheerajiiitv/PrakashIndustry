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
    sub_category = models.ManyToManyField('Category_under_Category')

    def __str__(self):
        return self.category_slug

class Category_under_Category(models.Model):
    category_name = models.CharField(max_length=100)


    def __str__(self):
        return self.category_name

from django.shortcuts import reverse

class Product(models.Model):
    product_name = models.CharField("Product Name",max_length=100,unique=True)
    slug = models.SlugField(unique=True,max_length=100)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_category = models.ManyToManyField('Category',related_name='category')
    product_quantity = models.PositiveIntegerField()
    product_rating = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

def _image_upload(instance, filename):
    return f'products/{instance.product.slug}/{filename}'


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product')
    image = models.ImageField(upload_to=_image_upload)
    alt_text = models.CharField(max_length=20)


    def __str__(self):
        return self.product.product_name


