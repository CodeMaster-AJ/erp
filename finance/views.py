from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def finance_dashboard(request):
    revenue = app_data.REVENUE_DATA
    expenses = app_data.EXPENSES
    gst_records = app_data.GST_RECORDS
    
    monthly_revenue = revenue[-1]['amount'] if revenue else 0
    monthly_expenses = sum(e['amount'] for e in expenses)
    net_profit = monthly_revenue - monthly_expenses
    gst_pending = sum(1 for g in gst_records if not g['filed'])
    
    exp_by_cat = {}
    for e in expenses:
        exp_by_cat[e['category']] = exp_by_cat.get(e['category'], 0) + e['amount']
    
    return render(request, 'finance/dashboard.html', {
        'monthly_revenue': monthly_revenue,
        'monthly_expenses': monthly_expenses,
        'net_profit': net_profit,
        'gst_pending': gst_pending,
        'exp_labels': list(exp_by_cat.keys()),
        'exp_values': list(exp_by_cat.values()),
    })

@login_required
def expenses(request):
    expenses = app_data.EXPENSES
    
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = int(request.POST.get('amount'))
        month = request.POST.get('month')
        description = request.POST.get('description')
        
        new_exp = {
            "id": len(expenses) + 1,
            "category": category, "amount": amount,
            "month": month, "description": description
        }
        app_data.EXPENSES.append(new_exp)
        return redirect('/finance/expenses/')
    
    by_category = {}
    for e in expenses:
        by_category[e['category']] = by_category.get(e['category'], 0) + e['amount']
    
    total = sum(e['amount'] for e in expenses)
    
    return render(request, 'finance/expenses.html', {
        'expenses': expenses,
        'by_category': by_category,
        'total': total,
    })

@login_required
def revenue(request):
    revenue_data = app_data.REVENUE_DATA
    orders = app_data.ORDERS
    
    product_revenue = {}
    for o in orders:
        product_revenue[o['product']] = product_revenue.get(o['product'], 0) + o['amount']
    
    monthly_revenue = [r['amount'] for r in revenue_data]
    monthly_labels = [r['month'] for r in revenue_data]
    
    total = sum(o['amount'] for o in orders)
    
    return render(request, 'finance/revenue.html', {
        'monthly_labels': monthly_labels,
        'monthly_revenue': monthly_revenue,
        'product_revenue': product_revenue,
        'total': total,
    })

@login_required
def schemes(request):
    schemes = app_data.SCHEMES
    
    total_funding = sum(s['amount'] for s in schemes)
    total_loans = sum(s['amount'] for s in schemes if s['type'] == 'Loan')
    total_grants = sum(s['amount'] for s in schemes if s['type'] == 'Grant')
    
    return render(request, 'finance/schemes.html', {
        'schemes': schemes,
        'total_funding': total_funding,
        'total_loans': total_loans,
        'total_grants': total_grants,
    })

@login_required
def gst(request):
    records = app_data.GST_RECORDS
    
    if request.method == 'POST':
        invoice_no = request.POST.get('invoice_no')
        customer = request.POST.get('customer')
        amount = int(request.POST.get('amount'))
        gst_rate = request.POST.get('gst_rate')
        gst_amount = int(amount * 0.05)
        total = amount + gst_amount
        date = request.POST.get('date')
        
        new_record = {
            "id": len(records) + 1,
            "invoice_no": invoice_no, "customer": customer,
            "amount": amount, "gst_rate": gst_rate,
            "gst_amount": gst_amount, "total": total,
            "date": date, "filed": False
        }
        app_data.GST_RECORDS.append(new_record)
        return redirect('/finance/gst/')
    
    filed = sum(1 for r in records if r['filed'])
    unfiled = len(records) - filed
    total_invoiced = sum(r['total'] for r in records)
    total_gst = sum(r['gst_amount'] for r in records)
    
    return render(request, 'finance/gst.html', {
        'records': records,
        'filed': filed,
        'unfiled': unfiled,
        'total_invoiced': total_invoiced,
        'total_gst': total_gst,
    })