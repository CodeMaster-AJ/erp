USERS = [
    {"id": 1, "name": "Admin User", "username": "admin", "password": "admin123", "role": "admin", "village": "All"},
    {"id": 2, "name": "Gurpreet Kaur", "username": "village_head", "password": "village123", "role": "village_head", "village": "Amritsar"},
    {"id": 3, "name": "Simran Sharma", "username": "trainer", "password": "train123", "role": "trainer", "village": "Ludhiana"},
    {"id": 4, "name": "Manpreet Kaur", "username": "worker", "password": "work123", "role": "worker", "village": "Amritsar"},
]

VILLAGES = [
    {"id": 1, "name": "Amritsar Unit", "district": "Amritsar", "head": "Gurpreet Kaur", "workers": 24, "status": "Active"},
    {"id": 2, "name": "Ludhiana Unit", "district": "Ludhiana", "head": "Harjit Singh", "workers": 18, "status": "Active"},
    {"id": 3, "name": "Patiala Unit", "district": "Patiala", "head": "Sukhjit Kaur", "workers": 12, "status": "Active"},
    {"id": 4, "name": "Bathinda Unit", "district": "Bathinda", "head": "Ranjit Kaur", "workers": 9, "status": "Setting Up"},
]

PRODUCTS = [
    {"id": 1, "name": "Achar (Pickle) - Mango", "category": "FMCG", "unit": "500g Jar", "price": 120, "stock": 340},
    {"id": 2, "name": "Handmade Phulkari Dupatta", "category": "Handicraft", "unit": "piece", "price": 1200, "stock": 45},
    {"id": 3, "name": "Organic Wheat Flour", "category": "Agro", "unit": "5kg bag", "price": 280, "stock": 210},
    {"id": 4, "name": "Sarson Ka Saag Mix", "category": "FMCG", "unit": "250g pack", "price": 85, "stock": 520},
    {"id": 5, "name": "Bamboo Basket (Medium)", "category": "Handicraft", "unit": "piece", "price": 350, "stock": 78},
]

ORDERS = [
    {"id": "ORD001", "customer": "Punjab Grocers Pvt Ltd", "type": "B2B", "product": "Achar - Mango", "qty": 50, "amount": 6000, "status": "Delivered", "date": "2025-04-10", "payment": "UPI"},
    {"id": "ORD002", "customer": "Ramesh Kumar", "type": "B2C", "product": "Phulkari Dupatta", "qty": 2, "amount": 2400, "status": "Shipped", "date": "2025-04-15", "payment": "COD"},
    {"id": "ORD003", "customer": "Meesho Platform", "type": "Marketplace", "product": "Organic Wheat Flour", "qty": 30, "amount": 8400, "status": "Processing", "date": "2025-04-18", "payment": "Net Banking"},
    {"id": "ORD004", "customer": "Amazon.in", "type": "Marketplace", "product": "Sarson Ka Saag Mix", "qty": 100, "amount": 8500, "status": "Pending", "date": "2025-04-20", "payment": "Net Banking"},
    {"id": "ORD005", "customer": "Gurdeep Kaur", "type": "B2C", "product": "Bamboo Basket", "qty": 1, "amount": 350, "status": "Delivered", "date": "2025-04-22", "payment": "UPI"},
]

EMPLOYEES = [
    {"id": 1, "name": "Gurpreet Kaur", "role": "Village Head", "village": "Amritsar", "skill": "Management", "salary": 18000, "joined": "2023-01-15", "status": "Active"},
    {"id": 2, "name": "Simran Sharma", "role": "Trainer", "village": "Ludhiana", "skill": "FMCG Production", "salary": 15000, "joined": "2023-03-01", "status": "Active"},
    {"id": 3, "name": "Manpreet Kaur", "role": "Worker", "village": "Amritsar", "skill": "Packaging", "salary": 9000, "joined": "2023-06-10", "status": "Active"},
    {"id": 4, "name": "Rajwinder Singh", "role": "Supervisor", "village": "Patiala", "skill": "Quality Control", "salary": 13000, "joined": "2023-02-20", "status": "Active"},
    {"id": 5, "name": "Harmeet Kaur", "role": "Worker", "village": "Amritsar", "skill": "Handicraft", "salary": 8500, "joined": "2024-01-05", "status": "Active"},
]

TRAINING_PROGRAMS = [
    {"id": 1, "title": "Pickle & Papad Making", "category": "FMCG", "duration": "10 days", "trainer": "Simran Sharma", "enrolled": 12, "status": "Active"},
    {"id": 2, "title": "Phulkari Embroidery", "category": "Handicraft", "duration": "15 days", "trainer": "Gurdeep Kaur", "enrolled": 8, "status": "Active"},
    {"id": 3, "title": "Organic Farming Basics", "category": "Agro", "duration": "7 days", "trainer": "Rajwinder Singh", "enrolled": 20, "status": "Completed"},
    {"id": 4, "title": "Hygiene & Food Safety", "category": "Compliance", "duration": "3 days", "trainer": "Simran Sharma", "enrolled": 30, "status": "Upcoming"},
]

EXPENSES = [
    {"id": 1, "category": "Raw Materials", "amount": 45000, "month": "April 2025", "description": "Mango, spices, wheat procurement"},
    {"id": 2, "category": "Logistics", "amount": 12000, "month": "April 2025", "description": "Delivery to distributors"},
    {"id": 3, "category": "Packaging", "amount": 8000, "month": "April 2025", "description": "Jars, bags, labels"},
    {"id": 4, "category": "Salaries", "amount": 85000, "month": "April 2025", "description": "All unit worker salaries"},
    {"id": 5, "category": "Utilities", "amount": 5500, "month": "April 2025", "description": "Electricity, water"},
]

REVENUE_DATA = [
    {"month": "Jan 2025", "amount": 180000},
    {"month": "Feb 2025", "amount": 210000},
    {"month": "Mar 2025", "amount": 195000},
    {"month": "Apr 2025", "amount": 245000},
]

DOCUMENTS = [
    {"id": 1, "name": "FSSAI License - Amritsar Unit", "type": "FSSAI", "expiry": "2026-03-31", "status": "Valid"},
    {"id": 2, "name": "GST Certificate", "type": "GST", "expiry": "Permanent", "status": "Valid"},
    {"id": 3, "name": "Trade License - Ludhiana", "type": "Trade", "expiry": "2025-12-31", "status": "Valid"},
    {"id": 4, "name": "FSSAI License - Patiala Unit", "type": "FSSAI", "expiry": "2025-06-30", "status": "Expiring Soon"},
]

DASHBOARD_STATS = {
    "total_villages": 4,
    "active_workers": 63,
    "monthly_revenue": 245000,
    "monthly_expenses": 155500,
    "active_training_programs": 2,
    "pending_orders": 2,
    "low_stock_alerts": 1,
    "compliance_alerts": 1,
}

VENDORS = [
    {"id": 1, "name": "Sharma Traders", "item": "Mango (Raw)", "rate": 45, "unit": "kg", "village": "Amritsar", "rating": 4.5, "status": "Active"},
    {"id": 2, "name": "Punjab Agro Supplies", "item": "Wheat", "rate": 28, "unit": "kg", "village": "Ludhiana", "rating": 4.2, "status": "Active"},
    {"id": 3, "name": "Bamboo Crafts Depot", "item": "Bamboo Strips", "rate": 120, "unit": "bundle", "village": "Patiala", "rating": 3.8, "status": "Active"},
    {"id": 4, "name": "Spice House", "item": "Mixed Spices", "rate": 350, "unit": "kg", "village": "Amritsar", "rating": 4.7, "status": "Active"},
]

RAW_MATERIALS = [
    {"id": 1, "name": "Raw Mango", "vendor": "Sharma Traders", "stock_kg": 500, "min_stock": 100, "unit": "kg", "last_ordered": "2025-04-10"},
    {"id": 2, "name": "Wheat Grain", "vendor": "Punjab Agro Supplies", "stock_kg": 1200, "min_stock": 300, "unit": "kg", "last_ordered": "2025-04-05"},
    {"id": 3, "name": "Mixed Spices", "vendor": "Spice House", "stock_kg": 45, "min_stock": 50, "unit": "kg", "last_ordered": "2025-04-01"},
    {"id": 4, "name": "Glass Jars (500g)", "vendor": "Packing Co", "stock_kg": 800, "min_stock": 200, "unit": "pieces", "last_ordered": "2025-04-12"},
    {"id": 5, "name": "Bamboo Strips", "vendor": "Bamboo Crafts Depot", "stock_kg": 30, "min_stock": 50, "unit": "bundles", "last_ordered": "2025-03-28"},
]

PRODUCTION_BATCHES = [
    {"id": "BATCH001", "product": "Achar - Mango", "category": "FMCG", "village": "Amritsar", "quantity": 200, "unit": "Jars", "start_date": "2025-04-15", "end_date": "2025-04-18", "status": "Completed", "assigned_to": "Harmeet Kaur"},
    {"id": "BATCH002", "product": "Organic Wheat Flour", "category": "Agro", "village": "Ludhiana", "quantity": 150, "unit": "Bags", "start_date": "2025-04-20", "end_date": "2025-04-22", "status": "In Progress", "assigned_to": "Manpreet Kaur"},
    {"id": "BATCH003", "product": "Phulkari Dupatta", "category": "Handicraft", "village": "Patiala", "quantity": 20, "unit": "Pieces", "start_date": "2025-04-25", "end_date": "2025-05-05", "status": "Scheduled", "assigned_to": "Sukhjit Kaur"},
    {"id": "BATCH004", "product": "Sarson Ka Saag Mix", "category": "FMCG", "village": "Amritsar", "quantity": 300, "unit": "Packs", "start_date": "2025-04-28", "end_date": "2025-04-30", "status": "Scheduled", "assigned_to": "Gurpreet Kaur"},
]

QUALITY_CHECKS = [
    {"id": 1, "batch": "BATCH001", "product": "Achar - Mango", "checked_by": "Rajwinder Singh", "date": "2025-04-18", "hygiene": "Pass", "packaging": "Pass", "expiry_marked": "Pass", "result": "Approved", "notes": "All clear"},
    {"id": 2, "batch": "BATCH002", "product": "Organic Wheat Flour", "checked_by": "Rajwinder Singh", "date": "2025-04-22", "hygiene": "Pass", "packaging": "Fail", "expiry_marked": "Pass", "result": "Rejected", "notes": "Bag seal issue — 10 bags returned"},
]

TRAINEES = [
    {"id": 1, "name": "Balwinder Kaur", "village": "Amritsar", "program": "Pickle & Papad Making", "enrolled_date": "2025-04-01", "progress": 75, "status": "In Progress"},
    {"id": 2, "name": "Sukhpreet Kaur", "village": "Amritsar", "program": "Pickle & Papad Making", "enrolled_date": "2025-04-01", "progress": 60, "status": "In Progress"},
    {"id": 3, "name": "Navneet Kaur", "village": "Ludhiana", "program": "Phulkari Embroidery", "enrolled_date": "2025-04-05", "progress": 40, "status": "In Progress"},
    {"id": 4, "name": "Prabhjot Kaur", "village": "Patiala", "program": "Organic Farming Basics", "enrolled_date": "2025-03-01", "progress": 100, "status": "Completed"},
    {"id": 5, "name": "Daljit Kaur", "village": "Amritsar", "program": "Organic Farming Basics", "enrolled_date": "2025-03-01", "progress": 100, "status": "Completed"},
]

CERTIFICATIONS = [
    {"id": 1, "trainee": "Prabhjot Kaur", "program": "Organic Farming Basics", "issued_date": "2025-03-30", "cert_id": "MPBB-CERT-001", "village": "Patiala"},
    {"id": 2, "trainee": "Daljit Kaur", "program": "Organic Farming Basics", "issued_date": "2025-03-30", "cert_id": "MPBB-CERT-002", "village": "Amritsar"},
]

TRAINING_SESSIONS = [
    {"id": 1, "program": "Pickle & Papad Making", "date": "2025-04-28", "time": "10:00 AM", "trainer": "Simran Sharma", "location": "Amritsar Unit", "attendees": 12},
    {"id": 2, "program": "Phulkari Embroidery", "date": "2025-04-29", "time": "2:00 PM", "trainer": "Gurdeep Kaur", "location": "Patiala Unit", "attendees": 8},
    {"id": 3, "program": "Hygiene & Food Safety", "date": "2025-05-01", "time": "9:00 AM", "trainer": "Simran Sharma", "location": "Amritsar Unit", "attendees": 30},
]

PURCHASE_ORDERS = []

NEW_BATCHES = []

NEW_QUALITY_CHECKS = []

DISTRIBUTORS = [
    {"id": 1, "name": "Singh Distributors", "region": "Amritsar", "contact": "9876543210", "products": ["Achar", "Flour"], "monthly_sales": 85000, "status": "Active"},
    {"id": 2, "name": "Kaur Traders Co", "region": "Ludhiana", "contact": "9812345678", "products": ["Dupatta", "Basket"], "monthly_sales": 42000, "status": "Active"},
    {"id": 3, "name": "Rural Fresh Pvt Ltd", "region": "Delhi NCR", "contact": "9988776655", "products": ["Saag Mix", "Flour"], "monthly_sales": 118000, "status": "Active"},
    {"id": 4, "name": "NRI Gifts Hub", "region": "Online", "contact": "info@nrigifts.com", "products": ["Dupatta", "Achar"], "monthly_sales": 0, "status": "New"},
]

CAMPAIGNS = [
    {"id": 1, "name": "Baisakhi Special Offer", "type": "Seasonal", "discount": "15%", "products": ["Achar", "Saag Mix"], "channel": "WhatsApp", "start": "2025-04-10", "end": "2025-04-15", "status": "Completed", "reach": 240},
    {"id": 2, "name": "Summer Cooling Products", "type": "Product Push", "discount": "10%", "products": ["Wheat Flour"], "channel": "SMS", "start": "2025-05-01", "end": "2025-05-31", "status": "Upcoming", "reach": 0},
    {"id": 3, "name": "Mother's Day Handicraft", "type": "Seasonal", "discount": "5%", "products": ["Dupatta", "Basket"], "channel": "WhatsApp + SMS", "start": "2025-05-11", "end": "2025-05-13", "status": "Upcoming", "reach": 0},
]

SCHEMES = [
    {"id": 1, "name": "PMEGP Loan", "type": "Loan", "amount": 500000, "received_date": "2023-06-01", "repayment_due": "2026-06-01", "status": "Active", "notes": "Machinery purchase - Amritsar unit"},
    {"id": 2, "name": "State Women SHG Grant", "type": "Grant", "amount": 150000, "received_date": "2024-01-15", "repayment_due": "N/A", "status": "Received", "notes": "No repayment needed"},
    {"id": 3, "name": "MUDRA Loan - Tarun", "type": "Loan", "amount": 200000, "received_date": "2024-03-10", "repayment_due": "2027-03-10", "status": "Active", "notes": "Working capital"},
]

GST_RECORDS = [
    {"id": 1, "invoice_no": "INV-2025-001", "customer": "Punjab Grocers Pvt Ltd", "amount": 6000, "gst_rate": "5%", "gst_amount": 300, "total": 6300, "date": "2025-04-10", "filed": True},
    {"id": 2, "invoice_no": "INV-2025-002", "customer": "Meesho Platform", "amount": 8400, "gst_rate": "5%", "gst_amount": 420, "total": 8820, "date": "2025-04-18", "filed": False},
    {"id": 3, "invoice_no": "INV-2025-003", "customer": "Amazon.in", "amount": 8500, "gst_rate": "5%", "gst_amount": 425, "total": 8925, "date": "2025-04-20", "filed": False},
]

CUSTOMERS = [
    {"id": 1, "name": "Punjab Grocers Pvt Ltd", "type": "B2B", "contact": "9876500001", "city": "Amritsar", "total_orders": 8, "total_spent": 52000, "last_order": "2025-04-10", "status": "Regular"},
    {"id": 2, "name": "Ramesh Kumar", "type": "B2C", "contact": "9876500002", "city": "Delhi", "total_orders": 3, "total_spent": 5600, "last_order": "2025-04-15", "status": "Regular"},
    {"id": 3, "name": "Amazon.in", "type": "Marketplace", "contact": "seller@amazon.in", "city": "Online", "total_orders": 12, "total_spent": 98000, "last_order": "2025-04-20", "status": "Premium"},
    {"id": 4, "name": "Meesho Platform", "type": "Marketplace", "contact": "seller@meesho.com", "city": "Online", "total_orders": 6, "total_spent": 42000, "last_order": "2025-04-18", "status": "Regular"},
]

TICKETS = [
    {"id": "TKT001", "customer": "Ramesh Kumar", "issue": "Product damaged in delivery", "priority": "High", "status": "Open", "created": "2025-04-16", "assigned_to": "Gurpreet Kaur"},
    {"id": "TKT002", "customer": "Punjab Grocers Pvt Ltd", "issue": "Wrong quantity delivered", "priority": "Medium", "status": "Resolved", "created": "2025-04-12", "assigned_to": "Simran Sharma"},
    {"id": "TKT003", "customer": "Amazon.in", "issue": "Label missing on 5 jars", "priority": "Low", "status": "In Progress", "created": "2025-04-21", "assigned_to": "Rajwinder Singh"},
]

NEW_TRAINEES = []

NEW_PROGRAMS = []

NEW_SESSIONS = []

ATTENDANCE = [
    {"id": 1, "employee_id": 1, "employee": "Gurpreet Kaur", "date": "2025-04-25", "status": "Present", "in_time": "09:00", "out_time": "17:30"},
    {"id": 2, "employee_id": 2, "employee": "Simran Sharma", "date": "2025-04-25", "status": "Present", "in_time": "09:15", "out_time": "17:00"},
    {"id": 3, "employee_id": 3, "employee": "Manpreet Kaur", "date": "2025-04-25", "status": "Absent", "in_time": "-", "out_time": "-"},
    {"id": 4, "employee_id": 4, "employee": "Rajwinder Singh", "date": "2025-04-25", "status": "Present", "in_time": "08:45", "out_time": "17:45"},
    {"id": 5, "employee_id": 5, "employee": "Harmeet Kaur", "date": "2025-04-25", "status": "Half Day", "in_time": "09:00", "out_time": "13:00"},
]

PAYROLL = [
    {"id": 1, "employee": "Gurpreet Kaur", "month": "April 2025", "basic": 18000, "bonus": 2000, "deductions": 1800, "net_pay": 18200, "status": "Paid", "paid_date": "2025-04-30"},
    {"id": 2, "employee": "Simran Sharma", "month": "April 2025", "basic": 15000, "bonus": 1500, "deductions": 1500, "net_pay": 15000, "status": "Paid", "paid_date": "2025-04-30"},
    {"id": 3, "employee": "Manpreet Kaur", "month": "April 2025", "basic": 9000, "bonus": 500, "deductions": 900, "net_pay": 8600, "status": "Pending", "paid_date": "-"},
    {"id": 4, "employee": "Rajwinder Singh", "month": "April 2025", "basic": 13000, "bonus": 1000, "deductions": 1300, "net_pay": 12700, "status": "Paid", "paid_date": "2025-04-30"},
    {"id": 5, "employee": "Harmeet Kaur", "month": "April 2025", "basic": 8500, "bonus": 0, "deductions": 425, "net_pay": 8075, "status": "Pending", "paid_date": "-"},
]

VOLUNTEERS = [
    {"id": 1, "name": "Amrita NGO Foundation", "type": "NGO Partner", "contact": "amrita@ngo.org", "focus": "Women Training", "since": "2023-01-01", "status": "Active"},
    {"id": 2, "name": "Dr. Navdeep Singh", "type": "Expert Volunteer", "contact": "9876501111", "focus": "Agro Techniques", "since": "2024-06-01", "status": "Active"},
    {"id": 3, "name": "Punjabi University Students", "type": "Intern Group", "contact": "placement@punjabiuniv.edu", "focus": "Marketing & Digital", "since": "2025-01-15", "status": "Active"},
]

COMPLIANCE_REMINDERS = [
    {"id": 1, "title": "FSSAI Renewal - Patiala Unit", "due_date": "2025-06-30", "type": "License", "priority": "High", "status": "Pending"},
    {"id": 2, "title": "GST Monthly Filing - May 2025", "due_date": "2025-05-20", "type": "GST", "priority": "High", "status": "Pending"},
    {"id": 3, "title": "Annual Trade License Renewal - Ludhiana", "due_date": "2025-12-31", "type": "Trade", "priority": "Medium", "status": "Pending"},
    {"id": 4, "title": "Quality Testing - Quarterly Check", "due_date": "2025-06-30", "type": "Quality", "priority": "Medium", "status": "Scheduled"},
]

SAFETY_CHECKS = [
    {"id": 1, "item": "Food Hygiene Standards", "unit": "Amritsar", "last_checked": "2025-04-01", "result": "Pass", "next_due": "2025-07-01"},
    {"id": 2, "item": "Packaging Sanitation", "unit": "Ludhiana", "last_checked": "2025-03-15", "result": "Pass", "next_due": "2025-06-15"},
    {"id": 3, "item": "Fire Safety Equipment", "unit": "Patiala", "last_checked": "2025-02-01", "result": "Fail", "next_due": "Immediate"},
    {"id": 4, "item": "Worker Safety Gear", "unit": "Amritsar", "last_checked": "2025-04-10", "result": "Pass", "next_due": "2025-07-10"},
]

ORG_INFO = {
    "name": "Mera Pind Balle Balle ERP",
    "address": "Village Kokri, District Amritsar, Punjab 143001",
    "gstin": "03AMPCB1234C1Z5",
    "contact": "9876500000",
    "email": "contact@mpbb-erp.org",
}