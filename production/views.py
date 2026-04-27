from django.shortcuts import render, redirect
import data as app_data

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def production_dashboard(request):
    batches = app_data.PRODUCTION_BATCHES
    raw_materials = app_data.RAW_MATERIALS
    quality_checks = app_data.QUALITY_CHECKS
    
    total_batches = len(batches)
    in_progress = sum(1 for b in batches if b['status'] == 'In Progress')
    low_stock = sum(1 for rm in raw_materials if rm['stock_kg'] < rm['min_stock'])
    quality_approved = sum(1 for qc in quality_checks if qc['result'] == 'Approved')
    quality_pass_rate = round((quality_approved / len(quality_checks) * 100) if quality_checks else 0)
    
    low_stock_items = [rm for rm in raw_materials if rm['stock_kg'] < rm['min_stock']]
    
    return render(request, 'production/dashboard.html', {
        'total_batches': total_batches,
        'in_progress': in_progress,
        'low_stock': low_stock,
        'quality_pass_rate': quality_pass_rate,
        'batches': batches,
        'low_stock_items': low_stock_items,
    })

@login_required
def raw_materials(request):
    raw_materials = app_data.RAW_MATERIALS
    vendors = app_data.VENDORS
    
    if request.method == 'POST':
        material = request.POST.get('material')
        vendor = request.POST.get('vendor')
        quantity = int(request.POST.get('quantity', 0))
        expected_date = request.POST.get('expected_date')
        
        new_po = {
            'id': len(app_data.PURCHASE_ORDERS) + 1,
            'material': material,
            'vendor': vendor,
            'quantity': quantity,
            'expected_date': expected_date,
            'status': 'Pending',
            'order_date': '2025-04-27'
        }
        app_data.PURCHASE_ORDERS.append(new_po)
        return redirect('/production/raw-materials/')
    
    return render(request, 'production/raw_materials.html', {
        'raw_materials': raw_materials,
        'vendors': vendors,
    })

@login_required
def batches(request):
    batches = app_data.PRODUCTION_BATCHES
    products = app_data.PRODUCTS
    employees = app_data.EMPLOYEES
    
    if request.method == 'POST':
        product = request.POST.get('product')
        category = request.POST.get('category')
        village = request.POST.get('village')
        quantity = int(request.POST.get('quantity', 0))
        unit = request.POST.get('unit')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        assigned_to = request.POST.get('assigned_to')
        
        new_batch = {
            'id': f'BATCH{str(len(app_data.PRODUCTION_BATCHES) + 1).zfill(3)}',
            'product': product,
            'category': category,
            'village': village,
            'quantity': quantity,
            'unit': unit,
            'start_date': start_date,
            'end_date': end_date,
            'status': 'Scheduled',
            'assigned_to': assigned_to
        }
        app_data.PRODUCTION_BATCHES.append(new_batch)
        return redirect('/production/batches/')
    
    return render(request, 'production/batches.html', {
        'batches': batches,
        'products': products,
        'employees': employees,
    })

@login_required
def quality(request):
    quality_checks = app_data.QUALITY_CHECKS
    
    total_checked = len(quality_checks)
    approved = sum(1 for qc in quality_checks if qc['result'] == 'Approved')
    rejected = sum(1 for qc in quality_checks if qc['result'] == 'Rejected')
    
    if request.method == 'POST':
        batch = request.POST.get('batch')
        product = request.POST.get('product')
        checked_by = request.POST.get('checked_by')
        date = request.POST.get('date')
        hygiene = request.POST.get('hygiene')
        packaging = request.POST.get('packaging')
        expiry_marked = request.POST.get('expiry_marked')
        notes = request.POST.get('notes')
        result = 'Approved' if hygiene == 'Pass' and packaging == 'Pass' and expiry_marked == 'Pass' else 'Rejected'
        
        new_qc = {
            'id': len(quality_checks) + 1,
            'batch': batch,
            'product': product,
            'checked_by': checked_by,
            'date': date,
            'hygiene': hygiene,
            'packaging': packaging,
            'expiry_marked': expiry_marked,
            'result': result,
            'notes': notes
        }
        app_data.QUALITY_CHECKS.append(new_qc)
        return redirect('/production/quality/')
    
    return render(request, 'production/quality.html', {
        'quality_checks': quality_checks,
        'total_checked': total_checked,
        'approved': approved,
        'rejected': rejected,
    })

@login_required
def inventory(request):
    products = app_data.PRODUCTS
    product_names = [p['name'] for p in products]
    stock_values = [p['stock'] for p in products]
    
    return render(request, 'production/inventory.html', {
        'products': products,
        'product_names': product_names,
        'stock_values': stock_values,
    })