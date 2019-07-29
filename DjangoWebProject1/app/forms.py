"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
#from .models import Post

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

#SEX_CHOICES= [
   # ('Male', 'Male'),
  #  ('Female', 'Female'),
   # ]

YEARS= [x for x in range(1940,3000)]
class MyForm(forms.Form):
 name = forms.CharField(label='Enter your name', max_length=50)
 lname = forms.CharField(label='Enter your last name', max_length=50)
 department = forms.CharField(label='Enter your department', max_length=50)
 age = forms.IntegerField(label='Enter your Age')
 birthdate = forms.DateField(label='Enter your birthdate', widget=forms.SelectDateWidget(years=YEARS))
#sex= forms.CharField(label='Gender', widget=forms.RadioSelect(choices=SEX_CHOICES))
#feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "50", 'rows': "10", }))
 
