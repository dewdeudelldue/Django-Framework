from django.urls import path
from django.db import models
from .import views 


class Courses(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)
    def __str__(self):
        return self.summary
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:course_id>',views.detail,name="detail")
]
