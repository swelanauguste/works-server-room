from django import forms

from .models import Port

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 51)]


class PortForm(forms.ModelForm):
    port = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)

    class Meta:
        model = Port
        fields = "__all__"
        exclude = ["slug"]
        widgets = {
            "vlan": forms.CheckboxSelectMultiple(attrs={"type": "checkbox",}),
        }
