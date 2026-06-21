from django.shortcuts import render, get_object_or_404
from .models import *

def get_cpp():
    return Department.objects.filter(name__icontains='цех подготовки производства').first()

def get_helmet_class(position):
    if not position:
        return 'default'
    
    position_lower = position.lower().strip()
    color_map = {
        # Белая каска (руководство)
        'руководитель': 'white',
        'начальник цпп': 'white',
        'заместитель': 'white',
        'главный инженер': 'white',
        'директор': 'white',
        
        # Жёлтая каска (начальники участков)
        'начальник участка': 'yellow',
        'начальник отдела': 'yellow',
        'начальник бюро': 'yellow',
        'начальник службы': 'yellow',
        
        # Оранжевая каска (мастера)
        'мастер': 'orange',
        'прораб': 'orange',
        'бригадир': 'orange',
        
        # Синяя каска (ИТР)
        'инженер': 'blue',
        'технолог': 'blue',
        'конструктор': 'blue',
        'экономист': 'blue',
        'табельщик': 'blue',
        'юрист': 'blue',
        
        # Красная каска (рабочие)
        'слесарь': 'red',
        'токарь': 'red',
        'сварщик': 'red',
        'грузчик': 'red',
        'водитель': 'red',
        'оператор': 'red',
        'крановщик': 'red',
        'электрик': 'red',
        'механик': 'red',
        
        # Зелёная каска (служащие)
        'специалист': 'green',
        'контролер': 'green',
        'диспетчер': 'green',
        'кладовщик': 'green',
        'секретарь': 'green',
        'бухгалтер': 'green',
    }
    for keyword, color in color_map.items():
        if keyword in position_lower:
            return color
    
    return 'default'

def index(request):
    cpp = get_cpp()
    news = News.objects.filter(is_published=True)[:4]
    leaders = Employee.objects.all()[:6]
    for leader in leaders:
        leader.helmet_color = get_helmet_class(leader.position)
    worktypes = WorkType.objects.all()
    vacancies = Vacancy.objects.filter(slots__gt=0)
    map_image = None
    
    return render(request, 'index.html', {
        'cpp': cpp,
        'news': news,
        'leaders': leaders,
        'worktypes': worktypes,
        'vacancies': vacancies,
        'map_image': map_image,
    })

def about(request):
    cpp = get_cpp()
    departments = Department.objects.all()
    employees = Employee.objects.all()
    for emp in employees:
        emp.helmet_color = get_helmet_class(emp.position)
    
    return render(request, 'about.html', {
        'cpp': cpp,
        'departments': departments,
        'employees': employees
    })

def equipment(request):
    cpp = get_cpp()
    equipments = Equipment.objects.all()
    return render(request, 'equipment.html', {
        'cpp': cpp,
        'equipments': equipments,
    })

def news(request):
    cpp = get_cpp()
    news = News.objects.filter(is_published=True)
    return render(request, 'news.html', {
        'cpp': cpp,
        'news': news,
    })

def news_detail(request, pk):
    cpp = get_cpp()
    item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {
        'cpp': cpp,
        'item': item,
    })

def vacancies(request):
    cpp = get_cpp()
    open_vacancies = Vacancy.objects.filter(slots__gt=0)
    closed_vacancies = Vacancy.objects.filter(slots=0)
    return render(request, 'vacancies.html', {
        'cpp': cpp,
        'open_vacancies': open_vacancies,
        'closed_vacancies': closed_vacancies,
    })

