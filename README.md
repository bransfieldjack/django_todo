# Django Practice

!["Django logo"](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/django-logo-positive.png)

### Configuration Setup

* sudo pip3 install django==1.11.
* django-admin startproject django_todo .
* python3 manage.py runserver $IP:$C9_PORT.
* Add a bash terminal alias to make it easier to start the app: alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT".
* django-admin startapp todo (starts an app - closed off piece of functionality/module).
* Open the views.py file, add the HttpResponse modelu from the shortcut library, and define a function which always takes a request parameter and returns a response. 
* Open the urls.py file in the main django_todo folder, and add the following: " url(r'^$', say_hello)" "from todo.views import say_hello".
* Add a templates folder to the todo folder, add a nlank html file with some boiler plate code. This will be called/accessed from the views.py file. 
* In order for any of the apps to work, they need to be added to the settings.py file under installed apps. 

### The admin panel

* To access the sqlite3 database, run: sqlite3 db.sqlite3.
* Django comes with a way of managing versions of tables and databases - migrations. 
* To manage migrations, use the command: python3 manage.py migrate (Migrations are versions of tables in the database).
* After running this command, use seelct * from django_migrations to view all the tables created. 
* Use: . headers , . mode column - displays in more readable format. 
* python3 manage.py createsuperuser - creates a new user, stored in auth_user table. 
* To access th admin panel, add /admin in front of the home view URL. 
* To create an sqlite3rc file, with .headers and .mode columns, add the new file to the ~/ directory. 

### Models

* A way for ouur python code to interact with our databases. 
* python3 manage.py makemigrations - creates config file for django to know what to do. 
* python3 manage.py migrate - creates a new table in the database called todo_item. 
* add, admin.site.register(Item) to the admin.py file, and check the admin console to confirm. 
* This will add items which are visible from the admin console, you can add more manually from the console if you wish. 
* In order to have the items display a more human readable version of the name, add the ' def __str__(self): return self.name ' to the end of the models file. 
* Templating can be used on the .html page to iterate through a list and display itsm from the model. 

### Form Input, template to model

* This is a way of posting data from the html form to the server. 
* This can also be done using django forms.

### Testing

* Pass TestCase as a parameter: 

        ``` def test_is_this_thing_on(self):
            self.assertEqual(1, 1) 
        ```

* Coverage: Allows us to generate reports that will tell use how much of our code has been tested. 
* Sudo pip3 install coverage. 
* coverage run --source=todo manage.py test.
* Coverage lets us see how much of our files have had tests run. 
* coverahe html -  generates a new folder 'htmlcov', inside is a file called index.html. 

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/coverage_report.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_forms.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_models.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_views.PNG)

### Deployment

* Hosting a Django application.
* Hosting a PostgreSQL database.
* Setup and create a heroku app.
* Create Heroku add-ons (PostgreSQL).
* Deploy a Django project.
* Automate further deployments.
* Secure and seperate dev code from live code.
* Project requirements, gunicorn(Python Web Server Gateway Interface HTTP server.) & psycopg2(Psycopg2 is a DB API 2.0 compliant PostgreSQL driver that is actively developed).
* Gunicorn: The package used to run the application on the server. 
* Gunicorn install: sudo pip3 install gunicorn.
* Psycopg2 install: sudo pip3 freeze install psycopg2.
* Requirements file, for deployment to heroku: pip3 freeze --local > requirements.txt.

 - Heroku Deployment:

* heroku create jackalack117-django-todo --region eu.

 - Inspecting apps on the dashboard:

* Allows to inspect all apps, do this from the dashboard - easier.