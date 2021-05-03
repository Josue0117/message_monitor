from django.forms import ModelForm
from users_manager.models import User

class SignupForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'
    