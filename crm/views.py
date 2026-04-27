from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def crm_dashboard(request):
    customers = app_data.CUSTOMERS
    tickets = app_data.TICKETS
    
    total_customers = len(customers)
    premium = sum(1 for c in customers if c['status'] == 'Premium')
    open_tickets = sum(1 for t in tickets if t['status'] == 'Open')
    resolved = sum(1 for t in tickets if t['status'] == 'Resolved')
    
    type_breakdown = {}
    for c in customers:
        type_breakdown[c['type']] = type_breakdown.get(c['type'], 0) + 1
    
    return render(request, 'crm/dashboard.html', {
        'total_customers': total_customers,
        'premium': premium,
        'open_tickets': open_tickets,
        'resolved': resolved,
        'type_labels': list(type_breakdown.keys()),
        'type_values': list(type_breakdown.values()),
        'recent_tickets': tickets[:3],
    })

@login_required
def customers(request):
    customers = app_data.CUSTOMERS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        cust_type = request.POST.get('type')
        contact = request.POST.get('contact')
        city = request.POST.get('city')
        
        new_cust = {
            "id": len(customers) + 1,
            "name": name, "type": cust_type, "contact": contact,
            "city": city, "total_orders": 0, "total_spent": 0,
            "last_order": "N/A", "status": "Regular"
        }
        app_data.CUSTOMERS.append(new_cust)
        return redirect('/crm/customers/')
    
    return render(request, 'crm/customers.html', {'customers': customers})

@login_required
def tickets(request):
    tickets = app_data.TICKETS
    customers = app_data.CUSTOMERS
    employees = app_data.EMPLOYEES
    
    if request.method == 'POST':
        customer = request.POST.get('customer')
        issue = request.POST.get('issue')
        priority = request.POST.get('priority')
        assigned_to = request.POST.get('assigned_to')
        
        new_ticket = {
            "id": f"TKT{str(len(tickets) + 1).zfill(3)}",
            "customer": customer, "issue": issue, "priority": priority,
            "status": "Open", "created": "2025-04-27", "assigned_to": assigned_to
        }
        app_data.TICKETS.append(new_ticket)
        return redirect('/crm/tickets/')
    
    open_tickets = [t for t in tickets if t['status'] == 'Open']
    in_progress = [t for t in tickets if t['status'] == 'In Progress']
    resolved = [t for t in tickets if t['status'] == 'Resolved']
    
    return render(request, 'crm/tickets.html', {
        'open_tickets': open_tickets,
        'in_progress': in_progress,
        'resolved': resolved,
        'customers': customers,
        'employees': employees,
    })