from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from courses.views import *

urlpatterns = [
    path('', home, name="Home"),
    path('register/', registerUser, name="RegisterUser"),
    path('lessons/<uuid:id>/', lessonsPage, name="LessonPage"),
    path('chapter/<uuid:id>/', displayLesson, name="DisplayLesson"),
    path('displayCourse/', displaySubject, name="DisplaySubject"),
    path('login/', loginPage, name="LoginPage"),
    path('logout/', logoutPage, name="LogoutPage"),
    path('profile/', profilePage, name="ProfilePage"),
    path('about/', about, name="about"),
    # ______________________________(Admin)_____________________________
    path('dj-admin/', adminUrl, name="AdminUrl"),
    path('adminLogin/', adminLogin, name="adminLogin"),
    path('userInfo/', userInfo, name="UserInfo"),
    path('subjectInfo/', subjectInfo, name="SubjectInfo"),
    path('lessonInfo/', lessonInfo, name="LessonInfo"),
    path('addLesson/', addLesson, name="AddLesson"),
    path('addSub/', addSubject, name="AddSubject"),
    path('addUser/', addUser, name="AddUser"),
    path('editUser/<int:id>/', editUser, name="EditUser"),
    path('editSubject/<uuid:id>/', editSubject, name="EditSubject"),
    path('editLesson/<uuid:id>/', editLesson, name="EditLesson"),
    path('deleteUser/<int:id>/', deleteUser, name="deleteUser"),
    path('deleteSubject/<uuid:id>/', deleteSubject, name="deleteSubject"),
    path('deleteLesson/<uuid:id>/', deleteLesson, name="deleteLesson"),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)