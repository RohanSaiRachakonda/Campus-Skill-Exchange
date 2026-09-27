from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Skill


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def home(request):
    return render(request, "home.html")
def add_skill(request):
    if request.method == "POST":
        skill_name = request.POST.get("skill_name")
        description = request.POST.get("description")
        category = request.POST.get("category")

        Skill.objects.create(
            user=request.user,
            skill_name=skill_name,
            description=description,
            category=category
        )

        return redirect("home")

    return render(request, "add_skill.html")
def profile(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, "profile.html", {"skills": skills})
def explore_skills(request):
    skills = Skill.objects.all()
    return render(request, "explore_skills.html", {"skills": skills})
def logout_view(request):
    logout(request)
    return redirect("login")