from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','email','addres_line_1','addres_line_2','country','city','state','order_note']    