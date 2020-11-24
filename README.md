# portfolio-django
> Create your own portfolio using Django and host on Azure Virtual Machine
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
- Open portfolio-django folder
- Open jobs\static folder
> PASTE YOUR IMAGE HERE
- Open jobs\template folder
- Open home.html
> Change COPY YOUR TEXT HERE with you own code
- Open detail.html
> Change COPY YOUR TEXT HERE with you own code
- Open Command Prompt and type:
```shell
C:> python manage.py makemigrations
C:> python manage.py migrate
C:> python manage.py collectstatic
C:> python manage.py createsuperuser
C:> python manage.py runserver
```
---
## What's Next?
> After successfully deploying app through Django offline, follow along on 29 November, 2020 at 3:00pm to 4:30pm for hosting on Azure VM
> https://teams.microsoft.com/l/meetup-join/19%3ameeting_MzhhYzQ2N2ItNGFkMC00OGJjLWI3ZmEtNDkxYWE2YzIxNGU4%40thread.v2/0?context=%7b%22Tid%22%3a%2284c31ca0-ac3b-4eae-ad11-519d80233e6f%22%2c%22Oid%22%3a%2261b56a05-8baf-4ceb-af98-5e2599339dfe%22%2c%22IsBroadcastMeeting%22%3atrue%7d
