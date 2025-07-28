# 🍽️ Django Delights

**Django Delights** is a learning project built to practice web development using Django. The application simulates a basic restaurant inventory and sales management system, allowing you to manage ingredients, menu items, recipes, and customer purchases.

This project focuses on the following skills:

- Django model design and database relationships  
- Working with views, forms, and templates  
- Authentication and access control  
- Generating reports using querysets and model data  

---

## 🎯 Project Goals

- Practice creating and managing models in Django  
- Implement forms and user input handling  
- Display database data using Django views and templates  
- Protect views with authentication  
- Explore relationships between models and perform queries  
- Display calculated financial summaries (revenue, cost, profit)  

---

## 🛠️ Features

- Add and manage ingredients with price and quantity  
- Create menu items and define their recipe requirements  
- Record customer purchases and automatically adjust inventory  
- View reports for:  
  - Current inventory  
  - Menu and required ingredients per item  
  - All purchases made  
  - Total revenue, ingredient cost, and profit  

---

## 🧰 Tech Stack

- Python 3  
- Django  
- HTML/CSS  
- SQLite (default Django database)  
- Git & GitHub  

---

## ▶️ Getting Started

To run this project locally, follow these steps:

```bash
# 1. Clone the repository
git clone git@github.com:doug1as/django_learning.git
cd django_learning

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Access the app at [http://localhost:8000/inventory](http://localhost:8000/inventory)

---

## 🔐 Authentication

- Only authenticated users can access most views  
- Includes login and logout pages  
- Uses Django's built-in authentication system  

---

## 🧱 Data Models

- **Ingredient**: name, price per unit, available quantity  
- **MenuItem**: name, price  
- **RecipeRequirement**: ingredient + quantity needed per menu item  
- **Purchase**: timestamp and menu item purchased  

---

## 📊 Available Views

- Inventory list  
- Menu items and their recipe requirements  
- Purchase history  
- Revenue, cost, and profit report  
- Forms to add ingredients, menu items, recipes, and purchases  

---

## 📎 Notes

This is a sample project created for educational purposes only. It is not intended for use in a production environment.

---

## 👤 Author

Douglas Rodrigues  
[GitHub: @doug1as](https://github.com/doug1as)
