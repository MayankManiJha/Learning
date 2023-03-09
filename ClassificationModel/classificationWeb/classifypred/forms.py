from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    
    def clean_message(self):
        username=self.cleaned_data.get("username")
        passowrd=self.cleaned_data.get("passowrd")
        return username