# How to Clone and Run This Django Project

1. Navigate to the folder where you want the project:
   cd "C:\Users\Dell\OneDrive\Desktop\vs files\sample"

2. Clone your repository:
   git clone https://github.com/Aadithyan-Creator/lab-django.git

3. Go into the project folder:
   cd lab-django/myapp

4. Create a virtual environment:
   python -m venv env

5. Activate the virtual environment:
   env\Scripts\activate

6. Upgrade pip (optional but recommended):
   python -m pip install --upgrade pip

7. Install dependencies from requirements.txt:
   pip install -r requirements.txt

8. Run migrations to create the database:
   python manage.py migrate

9. (Optional) Create a superuser for admin access:
   python manage.py createsuperuser

10. Run the Django development server:
    python manage.py runserver

11. Open your browser at http://127.0.0.1:8000/ to see the project running.
