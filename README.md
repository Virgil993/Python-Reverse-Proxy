# Python-Reverse-Proxy
An application that simulates a reverse proxy server written in python

To run the project , you must first have installed Python with the latest version, MySQL workbench and preferably Visual Studio Code with the Python extension installed. Follow the steps bellow to run the application:

1. First, open a terminal and run pip install pipenv to install a tool that can manage application dependecies in a virtual environment.
2. Download the Python Reverse Proxy zip then extract the folder in your preffered directory.
3. In a terminal go to the Python Reverse Proxy directory and run pipenv install django, this will create a virtual environment where django is installed.
4. To activate this virtual environment , in the terminal in the Python Reverse Proxy directory run pipenv shell.
5. Open Visual Studion Code and open the Python Reverse Proxy folder choose the virtual environment you just created as your interpreter.
6. In a terminal in VS Code run these 2 commands:python manage.py makemigrations and python manage.py migrate 

