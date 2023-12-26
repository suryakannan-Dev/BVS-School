"""
URL configuration for BVS_School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from School_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('student_login', views.studentLogin, name='studentLogin'),
    path('teacher_login', views.teacherLogin, name='teacherLogin'),
    path('parent_registration', views.parentRegistration, name='parentRegistration'),
    path('student_page/<str:student_name>/', views.studentPage, name='studentPage'),
    path('student_page/<str:student_name>/student_class', views.studentClass, name='studentClass'),
    path('student_page/<str:student_name>/student_timetable', views.studentTimeTable, name='studentTimeTable'),
    path('student_page/<str:student_name>/student_work', views.studentWork, name='/studentWork'),
    path('student_page/<str:student_name>/upload_work', views.uploadWork, name='/uploadWork'),
    path('upload', views.upload, name='upload'),
    path('student_page/<str:student_name>/student_profile', views.studentProfile, name='studentProfile'),

    path('teacher_page/<str:teacher_name>/', views.teacherPage, name='teacherPage'), 

    path('teacher_page/<str:teacher_name>/teacher_class', views.teacherClass, name='teacherClass'),
    path('teacher_page/<str:teacher_name>/teacher_timetable', views.teacherTimeTable, name='teacherTimeTable'),
    path('teacher_page/<str:teacher_name>/teacher_profile', views.teacherProfile, name='teacherProfile'),
    path('teacher_page/<str:teacher_name>/teacher_work', views.teacherWork, name='/teacherWork'),
    path('teacher_page/<str:teacher_name>/class_1', views.class1, name='class-1'),
    path('teacher_page/<str:teacher_name>/class_2', views.class2, name='class-2'),
    path('teacher_page/<str:teacher_name>/class_3', views.class3, name='class-3'),
    path('teacher_page/<str:teacher_name>/class_4', views.class4, name='class-4'),
    path('teacher_page/<str:teacher_name>/class_5', views.class5, name='class-5'),
    path('teacher_page/<str:teacher_name>/class_6', views.class6, name='class-6'),
    path('teacher_page/<str:teacher_name>/class_7', views.class7, name='class-7'),
    path('teacher_page/<str:teacher_name>/add_comment/<int:id>', views.addComment, name='addComment'),
    path('upload_comment/<int:id>', views.uploadComment, name='uploadComment'),
    path('blog', views.blog, name='blog'),
    path('game', views.game, name='game'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)