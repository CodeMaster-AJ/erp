# Mera Pind Balle Balle ERP

A comprehensive ERP (Enterprise Resource Planning) system for rural women empowerment startup in Punjab, India. Built with Django 4.x, TailwindCSS, Alpine.js, and Chart.js.

## 🌟 Features

### Core Modules
- **Authentication** - Session-based login with role management
- **Dashboard** - Central overview with stats, charts, and recent activities

### Production & Inventory
- Production batches with Kanban-style tracking
- Raw materials management
- Quality control checks
- Product inventory with stock visualization

### Training & Skills
- Training program management
- Trainee enrollment and progress tracking
- Training sessions scheduling
- Certification generation

### Sales & Marketing
- Order management
- Distributor network
- Marketing campaigns

### Finance
- Expense tracking
- Revenue reports
- Microfinance schemes management
- GST compliance

### CRM
- Customer profiles
- Support ticketing system

### HR & Workforce
- Employee profiles
- Attendance tracking
- Payroll system
- Volunteer coordination

### Compliance & Legal
- Document management
- Compliance reminders
- Health & safety checks

### Settings (Admin)
- Organization info management
- User management
- Village units configuration
- System preferences

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Frontend**: TailwindCSS 3.x (CDN)
- **Interactivity**: Alpine.js 3.x (CDN)
- **Charts**: Chart.js 4.x (CDN)
- **Icons**: Font Awesome 6.x (CDN)
- **Fonts**: Poppins + Inter (Google Fonts)
- **Data Storage**: In-memory Python dictionaries (data.py)

## 📋 Current Data Structure

All data is stored in `data.py` as Python dictionaries and lists:

```python
USERS = [...]          # User accounts
VILLAGES = [...]       # Village units
PRODUCTS = [...]        # Products inventory
ORDERS = [...]         # Sales orders
EMPLOYEES = [...]      # Staff/workers
TRAINING_PROGRAMS = [...]  # Training courses
EXPENSES = [...]       # Financial expenses
REVENUE_DATA = [...]   # Monthly revenue
DOCUMENTS = [...]      # Legal documents
DASHBOARD_STATS = {}   # Dashboard metrics

# Production
VENDORS = [...]        # Supplier vendors
RAW_MATERIALS = [...]  # Inventory materials
PRODUCTION_BATCHES = [...]
QUALITY_CHECKS = [...]

# Training
TRAINEES = [...]       # Enrolled learners
CERTIFICATIONS = [...]   # Issued certificates
TRAINING_SESSIONS = [...]

# Sales
DISTRIBUTORS = [...]
CAMPAIGNS = [...]

# Finance
SCHEMES = [...]        # Microfinance
GST_RECORDS = [...]    # Tax records

# CRM
CUSTOMERS = [...]      # Business customers
TICKETS = [...]       # Support tickets

# HR (New in v2)
ATTENDANCE = [...]    # Daily attendance
PAYROLL = [...]       # Salary records
VOLUNTEERS = [...]    # NGO/partners

# Compliance (New in v2)
COMPLIANCE_REMINDERS = [...]
SAFETY_CHECKS = [...]

# Organization (New in v2)
ORG_INFO = {...}
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install django
```

### Installation
```bash
cd mpbb_erp
python manage.py migrate  # Optional - for future database
python manage.py runserver
```

### Access
Open browser to: `http://127.0.0.1:8000/`

### Demo Credentials
| Role | Username | Password |
|------|----------|-----------|
| Admin | admin | admin123 |
| Village Head | village_head | village123 |
| Trainer | trainer | train123 |

## 📁 Project Structure

```
mpbb_erp/
├── manage.py              # Django entry point
├── data.py                # All application data
├── mpbb_erp/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  # Authentication & Dashboard
├── production/           # Production module
├── training/              # Training module
├── sales/                 # Sales module
├── finance/               # Finance module
├── crm/                   # CRM module
├── hr/                    # HR module
├── compliance/            # Compliance module
├── static/                # CSS, JS, images
└── templates/             # Base templates
```

## 🔑 Key URLs

| URL | Description |
|-----|-------------|
| `/login/` | User login |
| `/logout/` | User logout |
| `/dashboard/` | Main dashboard |
| `/settings/` | Admin settings |
| `/production/` | Production dashboard |
| `/production/raw-materials/` | Materials |
| `/production/batches/` | Batch Kanban |
| `/production/quality/` | Quality checks |
| `/production/inventory/` | Stock |
| `/training/` | Training dashboard |
| `/training/programs/` | Programs |
| `/training/trainees/` | Learners |
| `/training/sessions/` | Schedule |
| `/training/certifications/` | Certificates |
| `/sales/` | Sales dashboard |
| `/sales/orders/` | Orders |
| `/sales/distributors/` | Network |
| `/sales/campaigns/` | Marketing |
| `/finance/` | Finance dashboard |
| `/finance/expenses/` | Expenses |
| `/finance/revenue/` | Revenue |
| `/finance/schemes/` | Microfinance |
| `/finance/gst/` | Tax |
| `/crm/` | CRM dashboard |
| `/crm/customers/` | Customers |
| `/crm/tickets/` | Support |
| `/hr/` | HR dashboard |
| `/hr/employees/` | Staff |
| `/hr/attendance/` | Attendance |
| `/hr/payroll/` | Salaries |
| `/hr/volunteers/` | Partners |
| `/compliance/` | Compliance dashboard |
| `/compliance/documents/` | Documents |
| `/compliance/reminders/` | Alerts |
| `/compliance/safety/` | Safety |

## 🎨 UI Features

- ✅ Professional orange/green Punjab-inspired theme
- ✅ Fully responsive (mobile + desktop)
- ✅ Collapsible sidebar navigation
- ✅ Role-based menu highlighting
- ✅ Chart.js visualizations
- ✅ Alpine.js modals and interactivity
- ✅ Toast notifications
- ✅ Profile dropdown menu

## 📝 Future Improvements

### 1. Database Implementation
- Currently using in-memory Python dictionaries
- Needs: PostgreSQL/MySQL migration
- Use Django ORM models instead of data.py

### 2. Authentication & Security
- Add Django allauth for robust auth
- Implement password hashing (bcrypt)
- Add session management
- Role-based access control (permissions)

### 3. Data Persistence
- All changes lost on server restart
- Need database for persistent storage

### 4. Module Enhancements

**Production:**
- [ ] Add/Edit/Delete batches functionality
- [ ] Batch status workflow transitions
- [ ] Material consumption tracking
- [ ] Production yield calculations

**Training:**
- [ ] Program enrollment limits
- [ ] Progress auto-calculation
- [ ] Certificate PDF generation with QR codes

**Sales:**
- [ ] Order status workflow
- [ ] Payment integration
- [ ] Invoice generation

**Finance:**
- [ ] Automated payroll processing
- [ ] GST filing integration
- [ ] Budget vs actual reports

**HR:**
- [ ] Leave management
- [ ] Performance reviews
- [ ] Employee documents
- [ ] Attendance calendar view

**CRM:**
- [ ] Email/SMS notifications
- [ ] Customer segments
- [ ] Service level agreements

### 5. Reporting
- [ ] PDF report generation
- [ ] Export to Excel/CSV
- [ ] Scheduled reports via email

### 6. API Development
- [ ] RESTful API endpoints
- [ ] Mobile app integration
- [ ] Third-party integrations

### 7. Multi-tenancy
- [ ] Support multiple village units
- [ ] Unit-specific configurations

### 8. Notifications
- [ ] In-app notifications
- [ ] Email alerts
- [ ] WhatsApp/SMS integration

## 🤝 Contributing

This is an educational/demo project. For production use:

1. Implement proper database
2. Add authentication
3. Enhance security
4. Add testing
5. Deploy to production server

## 📄 License

Educational Use Only

## 👩‍💻 Credits

Built for: Mera Pind Balle Balle ERP
Location: Punjab, India
Purpose: Rural Women Empowerment Startup

---

*Empowering Rural Women Entrepreneurs*