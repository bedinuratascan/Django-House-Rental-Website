from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, forms, Select, FileInput
from django import forms
from home.models import UserProfile
from house.models import House, Category


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }


OPTIONS = [
    ('True', 'Evet'),
    ('False', 'Hayır'),
]


class HouseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    status = forms.ChoiceField(required=True, choices=OPTIONS)
    furnished = forms.ChoiceField(required=True, choices=OPTIONS)
    balconied = forms.ChoiceField(required=True, choices=OPTIONS)
    withintheSite = forms.ChoiceField(required=True, choices=OPTIONS)
    detail = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = House
        fields = ['category', 'title', 'keywords', 'description', 'slug', 'image',
                  'rent', 'detail', 'status', 'area', 'location',
                  'room', 'buildingFloor', 'floorLocation', 'furnished', 'balconied', 'heating', 'withintheSite',
                  'fromWho']

