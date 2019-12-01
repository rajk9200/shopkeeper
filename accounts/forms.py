from django import forms
from . models import Accounts
class SignupForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.EmailField(
            max_length=100,
            label='',
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Enter Email',
                    'class': 'form-control',

                }
            )
        )

    password = forms.CharField(max_length=100,
                                   label='',
                                   widget=forms.PasswordInput(
                                       attrs={
                                           'placeholder': 'Enter Password',
                                           'class': 'form-control',

                                       }
                                   )
                                   )
class ChangePassword(forms.Form):
    old_password = forms.CharField(max_length=100,
                               label='',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'placeholder': 'old Password',
                                       'class': 'form-control',

                                   }
                               )
                               )
    new_password = forms.CharField(max_length=100,
                               label='',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'placeholder': 'New Password',
                                       'class': 'form-control',

                                   }
                               )
                               )

    re_password = forms.CharField(max_length=100,
                               label='',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'placeholder': 'Repeat Password',
                                       'class': 'form-control',

                                   }
                               )
                               )

    def clean_re_password(self):
        re_password = self.cleaned_data.get("re_password")
        new_password = self.cleaned_data.get("new_password")

        if re_password!=new_password:
            raise forms.ValidationError("Password must be same!")
        return re_password