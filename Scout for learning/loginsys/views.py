# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from courses.models import Courses, CoursesToUsers

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            avatar = User.objects.get(username=request.user.username)
            args['ctu'] = CoursesToUsers.objects.filter(id_user_id=request.user.id).values("id_course_id", "finish")
            args['courses'] = Courses.objects.all()
            args['f_courses'] = CoursesToUsers.objects.filter(finish="1")
            args['avatar'] = avatar
            args['request'] = request
            return render_to_response('profile/profile.html', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('default_app/home.html', args)
    else:
        return render_to_response('default_app/home.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        p_password = request.POST.get('p_password', '')
        email = request.POST.get('email', '')
        if username and password and email:
            if p_password == password:
                userreg = User.objects.create_user(username, email, password)
                userreg.save()
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                avatar = User.objects.get(username=request.user.username)
                args['ctu'] = CoursesToUsers.objects.filter(id_user_id=request.user.id).values("id_course_id", "finish")
                args['courses'] = Courses.objects.all()
                args['f_courses'] = CoursesToUsers.objects.filter(finish="1")
                args['avatar'] = avatar
                args['request'] = request
                return render_to_response('profile/profile.html', args)
            else:
                args['register_error'] = "Пароли не совпадают"
                return render_to_response('default_app/home.html', args)
        else:
            args['register_error'] = "Все поля обязательны для заполнения"
            return render_to_response('default_app/home.html', args)
    else:
        return render_to_response('default_app/home.html', args)
