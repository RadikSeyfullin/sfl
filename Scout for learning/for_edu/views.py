from django.shortcuts import render
from django.contrib.auth.models import User

def for_edu(request):
    if request.user.is_authenticated():
        avatar = User.objects.get(username=request.user.username)
        z = (1)
        context = {
            'avatar': avatar,
            'z': z,
        }
    else:
        context = {

        }
    return render(request, 'for_edu/for-edu.html', context)
