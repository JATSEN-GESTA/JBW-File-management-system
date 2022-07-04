from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import Quotation, Code
from django.core.mail import send_mail



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def save(self):

        user = super().save(commit=False)
        user.name1 = self.cleaned_data.get('email')
        user.username = self.cleaned_data.get('username')
        user.save()

        send_mail('Registration Successful',
            f"""Congratulations you are now registered. Please double check your registration.\n
        """,
            
            'jbwemailtest@gmail.com',
            [f'{user.name1}'],
            fail_silently=False)

        return user

class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'

class Codenings(ModelForm):
    class Meta:
        model = Code
        fields =  '__all__'
