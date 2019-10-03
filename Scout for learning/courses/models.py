from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/courses', default='static/images/default_course.png', verbose_name='Изобразжение')
    author = models.CharField(max_length=150, default="None")
    url = models.CharField(max_length=200, default="None")
    def __str__(self):
        return self.title

class CoursesToUsers(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    finish = models.BooleanField()
