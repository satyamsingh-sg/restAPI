from django.contrib.auth.models import User
from django import forms
from django.db.models import fields

class Account(forms.ModelForm):
       
    class Meta:
        model=User
        fields=["username","email","password","first_name","last_name"]

        widgets={
            'username':forms.TextInput(
                attrs={
                    'type':'eamil',
                    'class':'form-control',
                    'id':'inputEmail4',
                    'placeholder':'User Name Exmple Shopindia@12',
                    'name':'name',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'type':'email',
                    'class':'form-control',
                    'id':'inputEmail4',
                    'placeholder':'Email',
                }
            ),
            'password':forms.TextInput(
                attrs={
                    'type':'password',
                    'class':'form-control',
                    'id':'inputPassword4',
                    'placeholder':'Password',
                    'name':'pass1',
                }
            ),
            'first_name':forms.TextInput(
                attrs={
                    'type':'first_name',
                    'class':'form-control',
                    'id':'inputPassword4',
                    'placeholder':'Password',
                    'name':'pass1',
                }
            ),
             'last_name':forms.TextInput(
                attrs={
                    'type':'last_name',
                    'class':'form-control',
                    'id':'inputPassword4',
                    'placeholder':'Password',
                    'name':'pass1',
                }
            )
        }


