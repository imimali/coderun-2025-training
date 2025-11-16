# Django - the fastest hand in the west
![](images/file-gsZddsgkZo8dl59okVHYLSoD.jpg)
Welcome to the Coderun 2025 Django tutorial. This tutorial will introduce you to the world of web development
in the context of Django.

## Why Django?
Django is a high-level, fast, scalable and secure web framework, with a clean and practical design. Many real world
platforms use Django, such as __Youtube__, __Instagram__, __Pinterest__, __Spotify__, and a lot more.

### BuT wHy NoT fLaSk?(or any other similar web framework)
Its popular use among big names that use it, like the above-mentioned should already partially answer
your questions. The critical aspect here is scalability. Django scales really well to apps that possibly have to support
millions of users. In comparison, Flask, for example, is a micro-framework, much more limited and more suitable for smaller projects.
Just as importantly, however, this is a framework that isn't very well covered in your usual university curricula, so
building apps in this one as well broadens your perspectives.

Having settled these, let's build stuff now!

## What we'll cover  

To get a grip on building any web app, the most important aspects are: 
- write views, define content, use templates to make it faster
- expose content through URL-s, configure paths
- communicate with the server (API calls, forms)
- persist data

## Installation
Django is a Python framework. You can download it from [here](https://www.python.org/downloads/).
Do yourself a favor and check the `Add Python to PATH` option there, it's gonna save you some time.

## Creating a virtual environment (optional, but highly recommended)
```shell
pip install virtualenv
```
Now create a virtual environment
```shell
python -m venv venv
```
or similarly
```shell
virtualenv venv
```
:bulb: If you're using Pycharm, you have the option to have this automatically created for you by creating a new project with the Django template.

Now activate the virtual environment
```shell
source venv/bin/activate
```
Or on windows
```shell
venv\Scripts\activate
```

This will isolate the current Python executable you use for this project only, so you won't tamper with the
global one and if you need to install something specific to this project only(with possibly conflicting versions with the system installation, for example)
then you can do it here only. This is simply good practice. But please *don't* upload this folder to your submissions,
neither do I need it nor it is making my job easier.

## And finally, we'll have Django
```shell
pip install Django
```
[pip](https://pypi.org/project/pip/) is the basic Python package manager. It lets you download libraries and frameworks, etc. It will do it in our local installation,
inside our virtual environment.

The following steps are automatically executed if you create a new Django app from Pycharm, but for clarity of exposition, it's
good for us to get through each step and to see how we create everything from scratch and not hide behind the big
shiny green button that just does everything for us.

```shell
django-admin startproject coderun
```
This will initialize a new project. The `django-admin` command is something that exists because we installed Django.
A project can contain multiple apps. We'll add apps to this project as well. For now, the directory structure
should look something like: 
```
coderun2025
├── coderun2025
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Let's see if it works:
```shell
python manage.py runserver
```
What we're doing here is calling the `python` executable to interpret the `manage.py` file with the `runserver` option.
If you see the screen with the rocket, that means you're good to go.

Let's create an app now:

```shell
python manage.py startapp coderun_demo
```
Now you should see something like this:
```
coderun2025
├── coderun2025
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── coderun_demo
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```

## Views, routing, URL-s
Django works with a specific version of the MVC (Model-View-Controller) pattern,
called MVT(Model-View-Template). Views are classes or functions that handle application logic. They generally receive
an HTTP request, handle it by possibly interacting with multiple subcomponents, models, etc. and return a response, generally
either as an HTTP page or as a JSON response. You can have multiple views for multiple use cases, and Django
decides what view to call based on routing. You'll hear more about routing a bit later.

The following examples are slightly different from what we did during the training
as I am adapting this readme from another tutorial, but I think it is a good exercise to map this
to the one we wrote.

Consider the following view:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='background-color:skyblue;display:flex;justify-content:center;'>Hello, code runner.</h1>")
```
As you can see, we can return complete HTML code as a string. But that's a bit savage, and not very maintainable. We'll see how to improve on this, but let's
make this view accessible.
You can add the following code to `demo/urls.py`:

```python
from .views import index
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
]
```
Then, the project `views.py` should look like:

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('coderun_demo.urls')),
]
```
:bulb: Now at http://127.0.0.1:8000/demo/index your view should be accessible. `include` made sure that
all views defined in `coderun_demo/urls.py` are accessible under the demo prefix.
Exercise: if you simply add another view with another URL to `coderun_demo/urls.py`, it should be accessible
under `/demo/your-view` without modifying the project URL-s file again.

_Why are URL-s important?
Having a consistent and clear URL pattern scheme is important for multiple reasons. Search Engine Optimisation (SEO) is one big factor. Crawler bots parse your website, and look at your URLs and contents and index your website based on certain rules that favor clear and meaningful URLs over random and meaningless ones. This indexing helps your website show up higher on search pages.
Consistent, meaningful and well-structured URL-s also help the educated user and make your site easier to navigate, not mentioning the fact that such URL-s will make your
website seem a lot more trustworthy and credible. Be nice, and make the effort of using consistent URL structures._

Let's come back to the view we wrote earlier with that piece of HTML. Let's be honest, God had no hand in the creation of that abhorrence. It looks ugly, it is not maintainable,
and just imagine the amount of pain one might have to go through if it was a more complex and bigger piece of HTML code that had to be edited manually as the unholy
Python string that it is right now, should you ever have to change anything about it. And what would we do if we'd have to insert dynamic content? There has to be a better way.

### Templates to the rescue!
Django lets you write your HTML code with the possibility of inserting dynamic content, and then
reference these files from within the views. These are called templates. They extend regular HTML with so-called template tags, that help
you insert your dynamic content defined as regular Python variables. On this most auspicious of occasions, we can
also dive into what a request object contains that the view receives.

Also make sure that your `TEMPLATES` dictionary in the `settings.py` of the project
has this key and value: `'DIRS': [BASE_DIR / 'templates']` to make sure Django
knows where to look for templates.

Let's add the following code to `coderun_demo/urls.py`:

```python
from django.shortcuts import render
... # the earlier views & imports

def inspect_request(request):
    return render(request, 'demo/index.html', context=dict(request=request))
```
then import and add this to the urlpatterns list of `demo/urls.py`:

```python
path('inspect/', inspect_request, name='inspect_request'),
```
Add a `demo` folder to `templates` and add the `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Proper Index page</title>
</head>
<body>
<h1>Hello, code runner</h1>
<div>
    {% if request.COOKIES %}
        <h2>I received some cookies</h2>
    {% else %}
        <h2> No cookies :(</h2>
    {% endif %}
</div>
<div>
    <h3>Path: <em>{{ request.path }}</em></h3>
    <h3>HTTP method: <em>{{ request.method }}</em></h3>
    <h3>Content-type: <em>{{ request.content_type }}</em></h3>
</div>
<div>
    <h3>Request params</h3>
    <ul>
        {% for param,value in request.GET.items %}
            <li>Param name: <b>{{ param }}</b> and Value: <b>{{ value }}</b></li>
        {% endfor %}
    </ul>
</div>

</body>
</html>
```
The content between the squiggles `{{ }}` is dynamic, while between `{% %}` you can add
control statements like ifs and fors, so that you can add dynamic content according to your needs. All these are
passed through the `context` parameter of the rendered view.
Access your website like http://127.0.0.1:8000/demo/inspect/?a=something&b=yesss and see how the
URL parameters show up.

## Forms
We saw how the website can communicate data towards users via views and templates, and saw partially how the user
can send information via request parameters. We'll explore a method to communicate in a bit more friendly way, without
requiring our users to know about editing URL parameters. Let's see how forms work.

We'll create a `forms.py` file in the demo folder, and add the following code:
```python
from django import forms


class UserDataForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=20)
    email = forms.EmailField(label='Email')
    weight = forms.IntegerField(label='Weight', min_value=0, max_value=300)
    gender = forms.ChoiceField(label='Gender', choices=[(1,'male'), (2,'female')],widget=forms.RadioSelect())
```
It comes handy that we can control the fields and input widgets for the form from Python code,
it makes form handling a lot easier.

Analogously, we'll add a new view(you should at this point know where):
```python
def register_user(request):
    user_data_form = UserDataForm()
    return render(request,'demo/user.html',context=dict(form=user_data_form))
```
and a new template in `user.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Page</title>
</head>
<body>
<h2>Register now!</h2>
<form method="post">
    {{ form.as_p }}
</form>
</body>
</html>
```
THe `form.as_p` is a method on the form object passed through the template context,
which renders the form content as an html `<p>` tag. You have other similar methods
on the form object such as `form.as_table`, etc.

This renders the form, now we can validate it, interact with it. But it still crashes on submitting it.

See the final version of [user.html](templates/user.html) and notice the 
```html
{% csrf_token %}
```
template tag. This is used to prevent cross-site request forgery. You can read more about it [here](https://docs.djangoproject.com/en/3.2/ref/csrf/).

## Databases, models

You can see a sample model class you can insert in models.py. Again, it's different from what we did during
the training because I'm adapting an older version of this tutorial. See the following class:
```python
from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    weight = models.IntegerField()
    gender = models.CharField(choices=[('male','male'),('male','female')],max_length=10,default='female')
```
And since we added the demo app to the installed apps of the project, (which looks like this now):
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coderun_demo' # notice this
]
```
we can tell Django to map our models to the database through its ORM.
Running 
```shell
python manage.py makemigrations
```
will populate the migrations folder with some code. Inspect it, study it. This is used by Django to keep track of database schema changes.
You can also inspect the `DATABASES` variable in `settings.py` to change the database instance.

But this still didn't change anything in our DB.
```shell
python manage.py migrate
```
Will run the afferent SQL code on your configured DB and actually make, alter or drop the tables
according to how you modified your code and made your migrations. The default DB vendor is sq lite, but you can
use anything else from Postgres to MySQL, MariaDB, it has support for all database vendors.

We'll also display our data now in the form, reiterating over it again, it'll look like:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Page</title>
</head>
<body>
<h2>Register now!</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>

<ul>
    {% for user in users %}
        <li>{{ user }}</li>
    {% endfor %}
</ul>
</body>
</html>
```
As you can see, the list of users displayed is now persisted.

This, however is not all. Models can have references to each other. You can read about how this works [here](https://docs.djangoproject.com/en/5.2/topics/db/models/)

## That's all, folks!
We learned how to create views, how to route them with proper URL patterns, we covered
sending data through forms and persisting data in a DB.
You can always refer to the original [documentation](https://www.djangoproject.com/).

And finally, if you have any questions, you can reach out to me in multiple ways.

<p align="center">
<a href="https://www.linkedin.com/in/imre-gergely-mali/" target="blank"><img align="center" src="https://user-images.githubusercontent.com/88904952/234979284-68c11d7f-1acc-4f0c-ac78-044e1037d7b0.png" alt="linkedin" height="50" width="50" /></a>
<a href="https://facebook.com/imi.mali.1" target="blank"><img align="center" src="https://user-images.githubusercontent.com/88904952/234980676-61bfb021-ecc8-48f7-88e6-34c1b06c4a58.png" alt="twitter" height="50" width="50" /></a> 
<a href="https://instagram.com/imimali/" target="blank"><img align="center" src="https://user-images.githubusercontent.com/88904952/234981169-2dd1e58f-4b7e-468c-8213-034ba62156c3.png" alt="instagram" height="50" width="50" /></a>
</p>