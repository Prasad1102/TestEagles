from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.
def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def profilePage(request):
  current_user = request.user
  context={'user':current_user}
  return render(request, "profile.html",context)

@login_required(login_url="/login")
def displaySubject(request):
  subject = Subject.objects.all()
  context = {'subject':subject}
  return render(request, "displaySubject.html", context)

def lessonsPage(request, id):
  print("I Come HEer")
  subject = Subject.objects.get(id=id)
  lessons = Lesson.objects.filter(subject_id=id)
  context = {'subject': subject, 'lessons': lessons}
  print("context", lessons)
  return render(request, "displayLessons.html", context)

def displayLesson(request, id):
  lesson = Lesson.objects.filter(id=id)
  context = {'lesson':lesson}
  return render(request, "lesson.html", context)

def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username=username).exists():
      messages.info(request, "Username Invalid Please Try Again")
      return redirect('/login')
    
    user = authenticate(username=username, password=password)
    if user is None:
      messages.info(request, "Invalid User")
      return redirect('/login')
    else:
      login(request, user)
      return redirect('/')
  return render(request, "login.html")

def logoutPage(request):
  logout(request)
  return redirect('/login')

def registerUser(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    user = User.objects.filter(username = username)
    if user.exists():
      messages.info(request, "User Already Exists")
      return redirect('/register')

    user = User.objects.create(
      username = username,
      first_name = first_name,
      last_name = last_name,
      email = email,
    )
    user.set_password(password)
    user.save()
    messages.info(request, "user created successfully")
  return render(request, "register.html")

# _________________________________{ADMIN}__________________________
@login_required(login_url="/adminLogin")
def adminUrl(request):
  return render(request, "admin/adminPanel.html")

def adminLogin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = User.objects.filter(username=username)
    if user.exists():
      user = authenticate(username=username, password=password)
      if user.is_superuser:
        login(request, user)
        return redirect('/dj-admin')
      else:
        messages.info(request, "You Were On Wrong Page")
        return redirect('/login')
    else:
      messages.info(request, "User Not Exist")
  return render(request, "admin/adminLogin.html")

def userInfo(request):
  users = User.objects.all()
  context = {'users':users}
  return render(request, "admin/userPanel.html", context)

def subjectInfo(request):
  subject = Subject.objects.all()
  context = {'subject':subject}
  return render(request, "admin/subjectPanel.html", context)

def lessonInfo(request):
  lessons = Lesson.objects.all()
  context = {'lessons':lessons}
  return render(request, "admin/lessonPanel.html", context)

def addSubject(request):
  if request.method == 'POST':
    subjectName = request.POST.get('subject_name')
    subjectImage = request.FILES.get('subject_image')
    if Subject.objects.filter(subject_name=subjectName).exists():
      messages.info(request, "Subject Already Exist")
    else:
      Subject.objects.create(
        subject_name  =subjectName,
        subject_image = subjectImage
      )
      messages.info(request, "Subject Added Successfully")
      return redirect("/addSub")
  return render(request, "admin/addSubject.html")

def addUser(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    if User.objects.filter(username=username).exists():
      messages.info(request, "Username Already Exist")
    else:
      user = User.objects.create(
        username = username,
        email = email,
        first_name = first_name,
        last_name = last_name
      )
      user.set_password(password)
      user.save()
      messages.info(request, "User Created")
      return redirect("/addUser")
  return render(request, "admin/addUser.html")

def addLesson(request):
  subjects = Subject.objects.all()
  context = {'subjects':subjects}
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    subject_id = request.POST.get('subject')
    subject = Subject.objects.get(id=subject_id)
    
    Lesson.objects.create(
      title = title,
      content = content,
      subject = subject
    )
    return redirect('/addLesson')
  return render(request, "admin/addLesson.html", context)

def editUser(request, id):
  user = User.objects.get(id=id)
  context = {'user':user}
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    user.username = username
    user.email = email
    user.first_name = first_name
    user.last_name = last_name

    user.save()
    return redirect('/userInfo')
  return render(request, "admin/editUser.html", context)

def editSubject(request, id):
  subject = Subject.objects.get(id=id)
  context = {'subject':subject}
  if request.method == 'POST':
    subject_name = request.POST.get('subject_name')

    subject.subject_name = subject_name
    subject.save()
    return redirect("/subjectInfo")
  return render(request, "admin/editSubject.html", context)

def editLesson(request, id):
  lesson = Lesson.objects.get(id=id)
  subjects = Subject.objects.all()
  print()
  context = {'lesson':lesson, 'subjects':subjects}
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    subject_id = request.POST.get('subject')
    subject = Subject.objects.get(id=subject_id)

    lesson.title = title
    lesson.content = content
    lesson.subject = subject

    lesson.save()
    return redirect('/lessonInfo')
  return render(request, "admin/editLesson.html", context)

def deleteUser(request, id):
  user = User.objects.get(id=id)
  user.delete()
  return redirect('/userInfo')

def deleteSubject(request, id):
  subject = Subject.objects.get(id=id)
  subject.delete()
  return redirect('/subjectInfo')

def deleteLesson(request, id):
  lesson = Lesson.objects.get(id=id)
  lesson.delete()
  return redirect('/lessonInfo')