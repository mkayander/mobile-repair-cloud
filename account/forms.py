from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

from account.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email",)
        field_classes = {'username': EmailField}
