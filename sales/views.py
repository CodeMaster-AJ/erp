from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def sales_dashboard(request):
    orders = app_data.ORDERS
    distributors = app_data.DISTRIBUTORS
    revenue_data = app_data.REVENUE_DATA
    
    total_revenue = sum(o['amount'] for o in orders)
    orders_this_month = len(orders)
    top_product = max(orders, key=lambda x: x['amount'])['product'] if orders else 'N/A'
    active_distributors = sum(1 for d in distributors if d['status'] == 'Active')
    
    revenue_labels = [r['month'] for r in revenue_data]
    revenue_values = [r['amount'] for r in revenue_data]
    
    region_sales = {}
    for d in distributors:
        region_sales[d['region']] = region_sales.get(d['region'], 0) + d['monthly_sales']
    
    recent_orders = orders[-5:]
    
    return render(request, 'sales/dashboard.html', {
        'total_revenue': total_revenue,
        'orders_this_month': orders_this_month,
        'top_product': top_product,
        'active_distributors': active_distributors,
        'revenue_labels': revenue_labels,
        'revenue_values': revenue_values,
        'region_labels': list(region_sales.keys()),
        'region_values': list(region_sales.values()),
        'recent_orders': recent_orders,
    })

@login_required
def orders(request):
    orders = app_data.ORDERS
    
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        customer = request.POST.get('customer')
        order_type = request.POST.get('type')
        product = request.POST.get('product')
        qty = int(request.POST.get('qty'))
        amount = int(request.POST.get('amount'))
        status = request.POST.get('status')
        date = request.POST.get('date')
        payment = request.POST.get('payment')
        
        new_order = {
            "id": order_id, "customer": customer, "type": order_type, "product": product,
            "qty": qty, "amount": amount, "status": status, "date": date, "payment": payment
        }
        app_data.ORDERS.append(new_order)
        return redirect('/sales/orders/')
    
    return render(request, 'sales/orders.html', {'orders': orders})

@login_required
def distributors(request):
    distributors = app_data.DISTRIBUTORS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        region = request.POST.get('region')
        contact = request.POST.get('contact')
        products = request.POST.get('products').split(',')
        monthly_sales = int(request.POST.get('monthly_sales', 0))
        
        new_dist = {
            "id": len(distributors) + 1,
            "name": name, "region": region, "contact": contact,
            "products": [p.strip() for p in products], "monthly_sales": monthly_sales, "status": "New"
        }
        app_data.DISTRIBUTORS.append(new_dist)
        return redirect('/sales/distributors/')
    
    names = [d['name'] for d in distributors]
    sales = [d['monthly_sales'] for d in distributors]
    
    return render(request, 'sales/distributors.html', {
        'distributors': distributors,
        'names': names,
        'sales': sales,
    })

@login_required
def campaigns(request):
    campaigns = app_data.CAMPAIGNS
    
    if request.method == 'POST':
        name = request.POST.get('name')
        campaign_type = request.POST.get('type')
        discount = request.POST.get('discount')
        products = request.POST.get('products')
        channel = request.POST.get('channel')
        start = request.POST.get('start')
        end = request.POST.get('end')
        
        new_campaign = {
            "id": len(campaigns) + 1,
            "name": name, "type": campaign_type, "discount": discount,
            "products": products.split(','), "channel": channel,
            "start": start, "end": end, "status": "Upcoming", "reach": 0
        }
        app_data.CAMPAIGNS.append(new_campaign)
        return redirect('/sales/campaigns/')
    
    return render(request, 'sales/campaigns.html', {'campaigns': campaigns})