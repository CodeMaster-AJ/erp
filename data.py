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