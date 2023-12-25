import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from MyApp.models import Login, userlogin, task


class DateInput(forms.DateInput):
    input_type = "date"

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label = 'password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')


class userloginform(forms.ModelForm):

    class Meta:
        model = userlogin
        fields = ('name','address','phone')


class DateInput(forms.DateInput):
    input_type = 'date'


class taskform(forms.ModelForm):
    DueDate = forms.DateField(widget=DateInput)
    class Meta:
        model = task
        fields=('Title','Description','DueDate','Category')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date = cleaned_data.get("DueDate")
    #     if date < datetime.date.today():
    #         raise forms.ValidationError("Date can't be in the past")
    #     return cleaned_data

