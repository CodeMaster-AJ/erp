from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def compliance_dashboard(request):
    docs = app_data.DOCUMENTS
    rem = app_data.COMPLIANCE_REMINDERS
    safety = app_data.SAFETY_CHECKS
    
    total = len(docs)
    expiring = sum(1 for d in docs if 'Expiring' in d.get('status', ''))
    pending = sum(1 for r in rem if r['status'] == 'Pending')
    safety_due = sum(1 for s in safety if s['result'] == 'Fail')
    
    high_priority = [r for r in rem if r['priority'] == 'High' and r['status'] == 'Pending']
    
    return render(request, 'compliance/dashboard.html', {
        'total': total, 'expiring': expiring, 'pending': pending, 'safety_due': safety_due,
        'high_priority': high_priority, 'reminders': rem[:4],
    })

@login_required
def documents(request):
    docs = app_data.DOCUMENTS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        dtype = request.POST.get('type')
        expiry = request.POST.get('expiry')
        
        new_doc = {
            "id": len(docs) + 1, "name": name, "type": dtype,
            "expiry": expiry, "status": "Valid"
        }
        app_data.DOCUMENTS.append(new_doc)
        return redirect('/compliance/documents/')
    
    return render(request, 'compliance/documents.html', {'documents': docs})

@login_required
def reminders(request):
    reminders = app_data.COMPLIANCE_REMINDERS
    
    if request.method == 'POST':
        title = request.POST.get('title')
        due = request.POST.get('due_date')
        dtype = request.POST.get('type')
        priority = request.POST.get('priority')
        
        new_rem = {
            "id": len(reminders) + 1, "title": title, "due_date": due,
            "type": dtype, "priority": priority, "status": "Pending"
        }
        app_data.COMPLIANCE_REMINDERS.append(new_rem)
        return redirect('/compliance/reminders/')
    
    reminders_sorted = sorted(reminders, key=lambda x: x['due_date'])
    return render(request, 'compliance/reminders.html', {'reminders': reminders_sorted})

@login_required
def safety(request):
    safety = app_data.SAFETY_CHECKS
    
    if request.method == 'POST':
        item = request.POST.get('item')
        unit = request.POST.get('unit')
        result = request.POST.get('result')
        
        new_check = {
            "id": len(safety) + 1, "item": item, "unit": unit,
            "last_checked": "2025-04-27", "result": result, "next_due": "2025-07-27"
        }
        app_data.SAFETY_CHECKS.append(new_check)
        return redirect('/compliance/safety/')
    
    passed = sum(1 for s in safety if s['result'] == 'Pass')
    total = len(safety)
    score = round((passed / total * 100) if total else 0)
    
    return render(request, 'compliance/safety.html', {'safety': safety, 'score': score})