# 🛒 Daily Basis - Django Web App

**Daily Basis** is a subscription-based Django web application designed to deliver essential daily items to users’ doorsteps — effortlessly and consistently. Unlike food delivery apps or e-commerce platforms, this app is focused on **routine and recurring needs**, helping users simplify their mornings and evenings.

---

## 🔍 Project Description

Many families require daily essentials like:
- 🥛 Milk, bread, eggs
- 📰 Newspapers
- 🧁 Morning bakery items
- 🌸 Puja flowers
- 🥣 Evening curd, fruits, groceries, etc.

**Daily Basis** allows users to:
- Register and manage their profile
- Subscribe to daily essentials (weekly/monthly)
- Schedule delivery time
- Add/remove/modify items for any specific day
- Receive daily deliveries hassle-free

This system aims to **save time**, **ensure consistency**, and become a reliable platform for everyday needs.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default Django DB for dev)
- **Templating Engine:** Django Template Language (DTL)

---

## 📸 Screenshots

> You can add screenshots inside a folder `assets/screenshots/` and link them like this:

```
![Home Page](assets/screenshots/homepage.png)
![Services](assets/screenshots/services.png)
![Contact Page](assets/screenshots/contact.png)
```

---

## 🚀 Features

- 🔐 User registration and authentication
- 📦 Subscription plans for recurring items
- 📋 Dynamic service listing
- 💬 Contact form with data handling
- 🎨 Gradient-themed modern UI

---

## 🏗️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/daily-basis.git
   cd daily-basis
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open in browser:  
   `http://127.0.0.1:8000/`

---

## 📂 Project Structure

```
daily-basis/
│
├── hello/              # Main Django app (models, views)
├── home/               # Home app (templates, views)
├── static/             # Static files (CSS, JS, images)
├── templates/          # Shared HTML templates
├── db.sqlite3          # Default SQLite database
├── manage.py
└── README.md           # ← Place this file here
```

---

## 🙌 Author

**Charan Kumar**  
[YouTube Channel](https://www.youtube.com/@charankumar)  
📧 [charankumar2666@gmail.com](mailto:charankumar2666@gmail.com)

---

## 📄 License

This project is for **practice and learning** purposes.  
You're free to modify and use it with proper attribution.
