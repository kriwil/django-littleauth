from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': _('email')}))

    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise forms.ValidationError(_('The email address is used. <a href="{0}">Login</a>?'.format(reverse('login'))))

    def save(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        return get_user_model().objects.register(email)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': _('email')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field', 'placeholder': _('****')}))

    def clean(self):
        data = super(LoginForm, self).clean()
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError(_('Invalid email or password.'))

        if not user.is_active:
            raise forms.ValidationError(_('User is inactive, please contact administrator.'))

        self.user = user
        return data

    def save(self, request):
        login(request, self.user)
