
from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser
from  django.contrib.auth import password_validation


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email','first_name','last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password_validation.validate_password(password1) is not None:
            raise forms.ValidationError("Password too commen")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email','first_name','last_name', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #
    #     user_exits = MyUser.objects.filter(email = email).first()
    #
    #     if not user_exits:
    #         raise forms.ValidationError("Invalid")
    #     else:
    #         if not user_exits.check_password(password):
    #             raise forms.ValidationError("Invalid")
    #     self.cleaned_data["user_obj"] = user_exits
    #     return super(UserLoginForm,self).clean()
from admin_interface.models import SubscribedUsers
from .models import CustomerReview
class AddSubscribedUserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input-email'}))

    class Meta:
        model = SubscribedUsers
        fields = ('__all__')


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=CustomerReview
#         fields = ('')


from .models import Address
class AddAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ('user','to_deliver')