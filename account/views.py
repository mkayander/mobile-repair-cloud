from django.urls import reverse_lazy
from django.views import generic

from account.forms import AccountCreationForm


class SignUpView(generic.CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
