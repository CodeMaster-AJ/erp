from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def hr_dashboard(request):
    employees = app_data.EMPLOYEES
    attendance = app_data.ATTENDANCE
    payroll = app_data.PAYROLL
    
    total = len(employees)
    present = sum(1 for a in attendance if a['status'] == 'Present')
    leave = sum(1 for a in attendance if a['status'] in ['Absent', 'Half Day'])
    pending = sum(1 for p in payroll if p['status'] == 'Pending')
    
    by_village = {}
    for e in employees:
        by_village[e['village']] = by_village.get(e['village'], 0) + 1
    
    return render(request, 'hr/dashboard.html', {
        'total': total, 'present': present, 'leave': leave, 'pending': pending,
        'village_labels': list(by_village.keys()), 'village_values': list(by_village.values()),
        'employees': employees, 'attendance': attendance[:5],
    })

@login_required
def employees(request):
    employees = app_data.EMPLOYEES
    
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        village = request.POST.get('village')
        skill = request.POST.get('skill')
        salary = int(request.POST.get('salary'))
        joined = request.POST.get('joined')
        
        new_emp = {
            "id": len(employees) + 1, "name": name, "role": role, "village": village,
            "skill": skill, "salary": salary, "joined": joined, "status": "Active"
        }
        app_data.EMPLOYEES.append(new_emp)
        return redirect('/hr/employees/')
    
    return render(request, 'hr/employees.html', {'employees': employees})

@login_required
def attendance(request):
    attendance = app_data.ATTENDANCE
    
    if request.method == 'POST':
        emp_id = int(request.POST.get('employee_id'))
        status = request.POST.get('status')
        for a in attendance:
            if a['employee_id'] == emp_id:
                a['status'] = status
        return redirect('/hr/attendance/')
    
    return render(request, 'hr/attendance.html', {'attendance': attendance, 'employees': app_data.EMPLOYEES})

@login_required
def payroll(request):
    payroll = app_data.PAYROLL
    
    if request.method == 'POST':
        emp_id = int(request.POST.get('employee_id'))
        for p in payroll:
            if p['id'] == emp_id:
                p['status'] = 'Paid'
                p['paid_date'] = '2025-04-27'
        return redirect('/hr/payroll/')
    
    total = sum(p['net_pay'] for p in payroll)
    return render(request, 'hr/payroll.html', {'payroll': payroll, 'total': total})

@login_required
def volunteers(request):
    volunteers = app_data.VOLUNTEERS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        vtype = request.POST.get('type')
        contact = request.POST.get('contact')
        focus = request.POST.get('focus')
        
        new_vol = {
            "id": len(volunteers) + 1, "name": name, "type": vtype,
            "contact": contact, "focus": focus, "since": "2025-04-27", "status": "Active"
        }
        app_data.VOLUNTEERS.append(new_vol)
        return redirect('/hr/volunteers/')
    
    return render(request, 'hr/volunteers.html', {'volunteers': volunteers})