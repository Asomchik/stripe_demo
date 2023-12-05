To run stripe_demo project:

1) Clone this repository to your computer.
2) Create a virtual environment inside the project directory (where *manage.py* is) and activate it.
3) Install dependencies from *requirements.txt*.
4) For demonstration purposes, this repository includes *.env*, which contains "secret" information that normally should
   not be visible.
5) Start django server (usually: python manage.py runserver). Visit it at http://127.0.0.1:8000/
6) Also, for demonstration, this repository includes db.sqlite3 prepopulated DB with some fake data.
   You can use it. There is a superuser for DB to get to admin panel at /admin/ URL. Login and password for superuser
   are set to "admin".  
7) The same project (with necessary settings changes) is deployed to web-server. You can see and use it
   at [stripe.asomchik.online](https://stripe.asomchik.online)