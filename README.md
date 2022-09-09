# Python-Reverse-Proxy
An application that simulates a reverse proxy server written in python

To run the project , you must first have installed Python with the latest version, MySQL workbench and preferably Visual Studio Code with the Python extension installed. Follow the steps bellow to run the application:

1. First, open a terminal and run pip install pipenv to install a tool that can manage application dependecies in a virtual environment.
2. Download the Python Reverse Proxy zip then extract the folder in your preffered directory.
3. In a terminal go to the Python Reverse Proxy directory and run pipenv install django, this will create a virtual environment where django is installed.
4. To activate this virtual environment , in the terminal in the Python Reverse Proxy directory run pipenv shell.
5. In the terminal you need to also run the command pip install mysqlclient to install mysql.
6. Open Visual Studion Code and open the Python Reverse Proxy folder choose the virtual environment you just created as your interpreter.
7. In the settings.py in the Python_Reverse_Proxy folder there is a dictionary called DATABASES , change the proprieties in that dictionary so you can connect your database to the project.
8. In a terminal in VS Code run these 2 commands:python manage.py makemigrations and python manage.py migrate
9. Then run the command python manage.py runserver 8080 and your server should be up and running. 

