from django.forms import ModelForm
from map.models import squirrels
class SquirrelForm(ModelForm):
        class Meta:
            model=squirrels
            fields='__all__'
