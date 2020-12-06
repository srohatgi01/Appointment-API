# Appointment System API
This is a very basic REST Application Programming Interface with multiple endpoints. 

# Tech Stack
The API is built using **Python** programming language using the web framework known as **Django** and **DRF** or **Django Rest Framework**. 

The sole reason of using Python as primary programming language for this API is -> Python was designed for readability, and has some similarities to the English language with influence from mathematics also it uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.

The preferred framwork has always been django over flask or any other as it gives full control and it is very powerful which is advantageous when creating an expandable backend service.

# Features
The Django project is named **cara-zorg** and the apps are named **api & v2**. The first version of code is in the api folder which have some unexpected errors that lead me to rewtrie the code in v2 django app.

API have 4 main endpoints - 
* __/api/v2/users/pk/__
  This endpoint is responsible for creating, getting, updating and deleting the users.
  
* __/api/v2/zorgs/[arguments]__
  This endpoint is responsible for creating, getting, updating and deleting the zorgs. Zorgs are in very basic terms, the sellers or the people you want to provide the services and get them users. This also supports filters and paginations as well as it gives 10 results at random from all the list using python's inbuilt oder library.
  
* __/api/v2/appointments/__ This endpoint is responsible for creating an appointment, getting detail, updating status and other details. **You cannot delete an appointment**. 

## v2
This app's code is divided into different files.
* models.py 
* serailizers.py
* views.py
* filters.py
* pagination.py
* urls.py


# How to run?
The prerequisite for running this repo is having Python 3.6 or higher, Django Framework, Django Rest Framework, django-filters, django-pagination, pillow and markdown.

Just clone the repo in your virtual environment (but Docker is preferred) and start server to verify you have no errors. 

Then run the **'makemigrations'** and **'migrate'** command followed by **'createsuperuser'** and you are good to go.

# Copyright-and-license
Code and documentation Copyright 2020 Sarthak Rohatgi. Under MIT License.

# Project Details
Project created by Sarthak Rohatgi. If you spot any bug or think of any feature or come across any bug/problems just create an issue and I will look into it as soon as possible.

# ❤️ Found this project useful?
If you found this project useful, then please consider giving it a ⭐ on Github and sharing it with your friends via social media.
