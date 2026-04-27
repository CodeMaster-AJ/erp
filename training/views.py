from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def training_dashboard(request):
    programs = app_data.TRAINING_PROGRAMS
    trainees = app_data.TRAINEES
    certifications = app_data.CERTIFICATIONS
    
    total_programs = len(programs)
    active_programs = sum(1 for p in programs if p['status'] == 'Active')
    total_trainees = len(trainees)
    certificates_issued = len(certifications)
    
    active_prog_list = [p for p in programs if p['status'] == 'Active']
    
    cats = {}
    for t in trainees:
        for p in programs:
            if p['title'] == t['program']:
                cat = p['category']
                cats[cat] = cats.get(cat, 0) + 1
                break
    category_labels = list(cats.keys())
    category_values = list(cats.values())
    
    return render(request, 'training/dashboard.html', {
        'total_programs': total_programs,
        'active_programs': active_programs,
        'total_trainees': total_trainees,
        'certificates_issued': certificates_issued,
        'active_prog_list': active_prog_list,
        'category_labels': category_labels,
        'category_values': category_values,
    })

@login_required
def programs(request):
    programs = app_data.TRAINING_PROGRAMS
    employees = [e for e in app_data.EMPLOYEES if e['role'] == 'Trainer']
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        duration = request.POST.get('duration')
        trainer = request.POST.get('trainer')
        enrolled = 0
        status = 'Upcoming'
        
        new_program = {
            'id': len(programs) + 1,
            'title': title,
            'category': category,
            'duration': duration,
            'trainer': trainer,
            'enrolled': enrolled,
            'status': status
        }
        app_data.TRAINING_PROGRAMS.append(new_program)
        return redirect('/training/programs/')
    
    return render(request, 'training/programs.html', {
        'programs': programs,
        'employees': employees,
    })

@login_required
def trainees(request):
    trainees = app_data.TRAINEES
    programs = app_data.TRAINING_PROGRAMS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        village = request.POST.get('village')
        program = request.POST.get('program')
        enrolled_date = request.POST.get('enrolled_date')
        
        new_trainee = {
            'id': len(trainees) + 1,
            'name': name,
            'village': village,
            'program': program,
            'enrolled_date': enrolled_date,
            'progress': 0,
            'status': 'In Progress'
        }
        app_data.TRAINEES.append(new_trainee)
        
        for p in app_data.TRAINING_PROGRAMS:
            if p['title'] == program:
                p['enrolled'] = p.get('enrolled', 0) + 1
                break
        
        return redirect('/training/trainees/')
    
    villages = list(set(t['village'] for t in trainees))
    prog_list = list(set(t['program'] for t in trainees))
    statuses = list(set(t['status'] for t in trainees))
    
    return render(request, 'training/trainees.html', {
        'trainees': trainees,
        'programs': programs,
        'villages': villages,
        'prog_list': prog_list,
        'statuses': statuses,
    })

@login_required
def sessions(request):
    sessions = app_data.TRAINING_SESSIONS
    programs = app_data.TRAINING_PROGRAMS
    employees = app_data.EMPLOYEES
    
    if request.method == 'POST':
        program = request.POST.get('program')
        date = request.POST.get('date')
        time = request.POST.get('time')
        trainer = request.POST.get('trainer')
        location = request.POST.get('location')
        attendees = int(request.POST.get('attendees', 0))
        
        new_session = {
            'id': len(sessions) + 1,
            'program': program,
            'date': date,
            'time': time,
            'trainer': trainer,
            'location': location,
            'attendees': attendees
        }
        app_data.TRAINING_SESSIONS.append(new_session)
        return redirect('/training/sessions/')
    
    return render(request, 'training/sessions.html', {
        'sessions': sessions,
        'programs': programs,
        'employees': employees,
    })

@login_required
def certifications(request):
    certifications = app_data.CERTIFICATIONS
    
    return render(request, 'training/certifications.html', {
        'certifications': certifications,
    })