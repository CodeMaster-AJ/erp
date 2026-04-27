from django.shortcuts import render, redirect
from django.http import HttpResponse
import data as app_data

def index(request):
    return redirect('/dashboard/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        for user in app_data.USERS:
            if user['username'] == username and user['password'] == password:
                request.session['user_id'] = user['id']
                request.session['username'] = user['username']
                request.session['name'] = user['name']
                request.session['role'] = user['role']
                request.session['village'] = user['village']
                return redirect('/dashboard/')
        
        return render(request, 'core/login.html', {'error': 'Invalid username or password'})
    
    if request.session.get('username'):
        return redirect('/dashboard/')
    
    return render(request, 'core/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('/login/')

def dashboard_view(request):
    if not request.session.get('username'):
        return redirect('/login/')
    
    stats = app_data.DASHBOARD_STATS
    orders = app_data.ORDERS[-5:]
    training_programs = app_data.TRAINING_PROGRAMS[:4]
    villages = app_data.VILLAGES[:4]
    
    revenue_labels = [r['month'] for r in app_data.REVENUE_DATA]
    revenue_values = [r['amount'] for r in app_data.REVENUE_DATA]
    
    expense_labels = [e['category'] for e in app_data.EXPENSES]
    expense_values = [e['amount'] for e in app_data.EXPENSES]
    
    return render(request, 'core/dashboard.html', {
        'stats': stats,
        'orders': orders,
        'training_programs': training_programs,
        'villages': villages,
        'revenue_labels': revenue_labels,
        'revenue_values': revenue_values,
        'expense_labels': expense_labels,
        'expense_values': expense_values,
    })