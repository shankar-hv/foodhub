# 🍔 FoodieHub - Django Food Ordering Website

FoodieHub is a modern food ordering web application developed using Django.  
Users can browse delicious foods, add items to cart, create accounts, and manage their profiles.

---

# 🚀 Features

✅ User Authentication  
- Signup  
- Login  
- Logout  

✅ Food Listing  
- Display food items with images  
- Food descriptions and pricing  

✅ Cart System  
- Add to cart  
- View cart items  
- Calculate total amount  

✅ User Profile  
- View username and email  

✅ Responsive UI  
- Modern Navbar  
- Attractive Food Cards  
- Hero Section  
- Footer Section  

✅ Admin Panel  
- Add/Edit/Delete foods  
- Upload food images  

---

# 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite3

---

# 📂 Project Structure

```bash
FoodieHub/
│
├── media/
│   └── foods/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── cart.html
│   └── profile.html
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Move Into Project Folder

```bash
cd FoodieHub
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\\Scripts\\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install django pillow
```

---

# 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

# ▶️ Run Server

```bash
python manage.py runserver
```

Open browser:

```bash
http://127.0.0.1:8000/
```

---

# 🖼️ Media Configuration

Add in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Add in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
```

---

# 🍕 Sample Foods

- Burger
- Pizza
- Pasta
- Dosa
- Biryani
- Momos

---

# 🔮 Future Enhancements

- Online Payment Gateway
- Food Search
- Category Filters
- Order Tracking
- Wishlist
- Dark Mode
- Quantity Controls
- Razorpay Integration

---

# 📚 Learning Outcomes

Through this project, I learned:

- Django Authentication
- Django Models
- CRUD Operations
- Media Handling
- Template Inheritance
- Responsive UI Design
- Bootstrap Integration

---

# 👨‍💻 Developer

H V Shankar  
B.E CSE Student  
City Engineering College, Bengaluru

GitHub: shankar-hv

---

# ⭐ Conclusion

FoodieHub is a beginner-friendly Django project that demonstrates a complete food ordering workflow with authentication, cart functionality, and responsive UI design.
