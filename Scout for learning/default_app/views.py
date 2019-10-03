from django.shortcuts import render
from catalog.models import Catalog
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated():
        avatar = User.objects.get(username=request.user.username)
        context = {
            'avatar': avatar,
            'request': request,
        }
    else:
        context = {

        }
    return render(request, 'default_app/home.html', context)
