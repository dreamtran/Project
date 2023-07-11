from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record, Deal

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)

class AddDealForm(forms.ModelForm):
    deal_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Deal name", "class":"form-control"}), label="")
    pipeline = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pipe line", "class":"form-control"}), label="")
    deal_owner = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Deal owner", "class":"form-control"}), label="")
    close_day = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Close day", "class":"form-control"}), label="")
    amount = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount", "class":"form-control"}), label="")
    
    class Meta:
        model = Deal
        exclude = ("user",)