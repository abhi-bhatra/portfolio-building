# portfolio-django
> Create your own portfolio using Django
## 
## Steps
- install Python using 'https://www.python.org/'
- Open Command Prompt and type: 
```shell
C:> python -m pip install virtualenv
C:> python -m venv my_lab_2
C:> my_lab_2\Scripts\activate
C:> cd Desktop
C:> python -m pip install django pillow python-git
C:> git clone https://github.com/abhi-bhatra/portfolio-django.git
C:> cd portfolio-django
```
```shell
C:> python manage.py makemigrations
C:> python manage.py migrate
C:> python manage.py collectstatic
C:> python manage.py createsuperuser
C:> python manage.py runserver
```
