from django import forms
from django.forms import widgets
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere", required=False)
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        required=False, queryset=models.RoomType.objects.all(), empty_label="Any Kind"
    )
    country = CountryField(default="KR").formfield()
    guests = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    bathrooms = forms.IntegerField(required=False)
    bath = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    supehost = forms.BooleanField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    houoserules = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Houoserule.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
