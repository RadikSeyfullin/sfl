from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from courses.models import Courses, CoursesToUsers

def profile(request):
    if request.user.is_authenticated():
        avatar = User.objects.get(username=request.user.username)
        ctu = CoursesToUsers.objects.filter(id_user_id=request.user.id).values("id_course_id", "finish")
        courses = Courses.objects.all()
        f_courses = CoursesToUsers.objects.filter(finish="1")

        context = {
            'f_courses': f_courses,
            'ctu': ctu,
            'courses': courses,
            'avatar': avatar,
        }
        return render(request, 'profile/profile.html', context)
    else:
        context = {
        }
        return render(request, 'default_app/home.html', context)
