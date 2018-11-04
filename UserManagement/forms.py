from .models import AddNewUser
from django import forms

class AddNewUser(forms.ModelForm):

    class Meta:
        model = AddNewUser
        fields = ('FullName','Email','Username','PhoneNumber','ProfileImage','AddressLine1','AddressLine2','City','State','Country','Zip')
        hidden_field = ('CreatedOn' ,  'active')