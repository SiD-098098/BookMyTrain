## 🚆 BookMyTrain – Train Booking System

A web-based train ticket booking system built with Django (backend) and HTML/CSS/JS (frontend). It allows users to search trains, view availability, and book seats.

---

### 📂 Project Structure

```
main/
├── main/              # Django backend
├── frontend/             # HTML/CSS/JS frontend
├── manage.py
└── README.md
```

---

## 💪 Setup Instructions

### ⚖️ Requirements

- Python 3.8+
- pip
- Git
- Virtual environment (`venv`)

---

### ⚙️ Backend Setup (Django)

1. **Clone the repository**

   ```bash
   git clone https://github.com/SiD-098098/BookMyTrain.git
   cd BookMyTrain
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # source myenv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**

   ```bash
   python manage.py runserver
   ```

7. The API is now live at:\
   `http://127.0.0.1:8000/`

---

### 🌐 Frontend Setup

If you’re hosting it separately:

1. Open `frontend/index.html` in your browser

2. Or deploy it (see hosting section below)

---

## 🚀 Deployment

### ✅ Backend on Render

1. Push your backend to a public GitHub repo

2. Go to [Render](https://render.com/)

3. Create a new **Web Service**

4. Set:

   - **Build Command:** `pip install -r requirements.txt && python manage.py migrate`
   - **Start Command:** `gunicorn projectname.wsgi`
   - **Environment variables:** Set `DEBUG=False` and `ALLOWED_HOSTS` accordingly
   - **Database:** SQLite (for testing) or PostgreSQL (for production)

5. Enable CORS in `settings.py`:

   ```python
   CORS_ALLOWED_ORIGINS = ["https://your-frontend.netlify.app"]
   ```

---

### ✅ Frontend on Netlify 

1. Zip your `frontend/` folder
2. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
3. Drag and drop the zipped folder
4. Netlify will instantly host your site and give you a live URL

---

## 📝 Notes

- Authentication is via Django TokenAuth (`Authorization: Token <your_token>`)
- Admin actions like making a train/ deleting a train are supported in the API but don't have a frontend component.
- By default CORS ALLOW ALL ORIGINS is true (for demo purposes), set to false in production environments.
- Live hosted version uses Render and Netlify. Render backend is pretty laggy (free tier).


