from django import forms
from .models import Elementos, Elementos1, Elementos2


class ElementForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = '__all__'

class ElementForm1(forms.ModelForm):
    class Meta:
        model = Elementos1
        fields = '__all__'

class ElementForm2(forms.ModelForm):
    class Meta:
        model = Elementos2
        fields = '__all__'


#class OrderForm(forms.ModelForm):

#      class Meta:
#      model = Order
#      fields = ['name', 'order_quantity']