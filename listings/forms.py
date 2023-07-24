from django.forms import ModelForm
from .models import Listings

class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            "title",
            "price",
            "num_bed",
            "num_bath",
            "sq_foot",
            "address",
            "image"
        ]