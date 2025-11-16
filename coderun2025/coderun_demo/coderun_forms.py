import  django.forms as forms

class FruitForm(forms.Form):
    fruit_name = forms.CharField(label='Name', max_length=20)
    weight = forms.FloatField(label='Weight',min_value=0.0)
    color = forms.ChoiceField(label='Color',choices=[(1,'red'),(2,'green'),(3,'white'),(4,'purple'),(5,'yellow'),(6,'blue')])
