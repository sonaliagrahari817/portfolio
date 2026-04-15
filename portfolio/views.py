# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    skills = [
        {'name': 'Python', 'level': 70},
        {'name': 'Django', 'level': 75},
        {'name': 'HTML & CSS', 'level': 90},
        {'name': 'JavaScript', 'level': 80},
        {'name': 'SQL / MySQL', 'level': 70},
        {'name': 'React', 'level': 60},
        {'name': 'Java', 'level': 85},
       
    ]
    return render(request, 'portfolio/about.html', {'skills': skills})

def projects(request):
   projects_list = [
    {
        'title': 'Portfolio Website',
        'description': 'A modern personal portfolio built using Django with responsive UI and clean design.',
        'tech': 'Django, HTML, CSS',
        'github': 'https://github.com/sonaliagrahari817/portfolio',
        'color': '#6C63FF'
    },
    {
        'title': 'To-Do App',
        'description': 'A task management app to add, update and delete tasks.',
        'tech': 'HTML,CSS,JS',
        'github': 'https://github.com/sonaliagrahari817/todo-js.git',
        'color': '#FF6584'
    },
    {
        'title': 'Student Burnout Detection',
        'description':'A full-stack burnout detection web app built using Flask that analyzes user inputs, calculates a burnout score, and classifies burnout levels with personalized feedback.',
        'tech': 'Python, Flask, Rule-Based-Logics',
        'github': 'https://github.com/sonaliagrahari817/burnout-detection-app.git',
        'color': '#43B89C'
    },
    {
        'title': 'Myntra Clone',
        'description': 'Frontend clone of Myntra website with responsive design and UI components.',
        'tech': 'HTML, CSS, JavaScript',
        'github': 'https://github.com/sonaliagrahari817/myntraClone-js.git',
        'color': '#FF6F91'
    },
  ]
   return render(request, 'portfolio/projects.html', {'projects': projects_list})

def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("----- NEW MESSAGE -----")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("-----------------------")

        success = True

    return render(request, 'portfolio/contact.html', {'success': success})