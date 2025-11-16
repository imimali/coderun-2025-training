from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .coderun_forms import FruitForm
from .models import Fruit

def hello(request):
    return HttpResponse("<h1>Title</h1><h2>Subtitle1</h2><h2>Subtitle2</h2><h2>Subtitle3</h2>")

def hello_with_templates(request):

    if request.method == 'POST':
        post_form = FruitForm(request.POST)
        if post_form.is_valid():
            name = post_form.cleaned_data['fruit_name']
            weight = post_form.cleaned_data['weight']
            color = post_form.cleaned_data['color']
            fruit = Fruit(name=name,weight=weight,color=color)
            fruit.save()

    form = FruitForm()
    return render(request, 'coderun_demo/index.html',
                  context=dict(name='Sherlock',
                               age='35',
                               display_something=False,
                               request=request,
                               form=form,
                               fruits=Fruit.objects.all()
                               ))
