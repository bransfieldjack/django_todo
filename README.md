# Django Practice

!["Django logo"](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/django-logo-positive.png)

## Configuration Setup

* sudo pip3 install django==1.11.
* django-admin startproject django_todo .
* python3 manage.py runserver $IP:$C9_PORT.
* Add a bash terminal alias to make it easier to start the app: alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT".
* django-admin startapp todo (starts an app - closed off piece of functionality/module).
* Open the views.py file, add the HttpResponse modelu from the shortcut library, and define a function which always takes a request parameter and returns a response. 
* Open the urls.py file in the main django_todo folder, and add the following: " url(r'^$', say_hello)" "from todo.views import say_hello".
* Add a templates folder to the todo folder, add a nlank html file with some boiler plate code. This will be called/accessed from the views.py file. 
* In order for any of the apps to work, they need to be added to the settings.py file under installed apps. 

## The admin panel

* To access the sqlite3 database, run: sqlite3 db.sqlite3.
* Django comes with a way of managing versions of tables and databases - migrations. 
* To manage migrations, use the command: python3 manage.py migrate (Migrations are versions of tables in the database).
* After running this command, use seelct * from django_migrations to view all the tables created. 
* Use: . headers , . mode column - displays in more readable format. 
* python3 manage.py createsuperuser - creates a new user, stored in auth_user table. 
* To access th admin panel, add /admin in front of the home view URL. 
* To create an sqlite3rc file, with .headers and .mode columns, add the new file to the ~/ directory. 

## Models

* A way for our python code to interact with our databases. 
* python3 manage.py makemigrations - creates config file for django to know what to do. 
* python3 manage.py migrate - creates a new table in the database called todo_item. 
* add, admin.site.register(Item) to the admin.py file, and check the admin console to confirm. 
* This will add items which are visible from the admin console, you can add more manually from the console if you wish. 
* In order to have the items display a more human readable version of the name, add the ' def __str__(self): return self.name ' to the end of the models file. 
* Templating can be used on the .html page to iterate through a list and display itsm from the model. 

## Form Input, template to model

* This is a way of posting data from the html form to the server. 
* This can also be done using django forms.

## Testing

* Pass TestCase as a parameter: 

        ~~~ 
        
        def test_is_this_thing_on(self):
            self.assertEqual(1, 1) 
            
        ~~~

* Coverage: Allows us to generate reports that will tell use how much of our code has been tested. 
* Sudo pip3 install coverage. 
* coverage run --source=todo manage.py test.
* Coverage lets us see how much of our files have had tests run. 
* coverahe html -  generates a new folder 'htmlcov', inside is a file called index.html. 

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/coverage_report.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_forms.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_models.PNG)

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/testing/test_views.PNG)

## Deployment

!["Coverage statistics: "](https://s3-ap-southeast-2.amazonaws.com/django-todo/deployment/heroku_logo.png)

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

### Making code deployment ready

* Heroku Deployment:

* heroku create jackalack117-django-todo --region eu.
* Inspecting apps on the dashboard:
* Allows to inspect all apps, do this from the dashboard - easier.

* Creating a new database on heroku:

* Heroku Addons: Allows us to create and manage addons for applications.
* heroku addons:create heroku-postgresql:hobby-dev.
* hobby-dev: specifies a free account level subscription. 

* Connecting to the remote database:

* dj_database_url: A package that parses database URIs
* Database URI can be found in heroku config vars. Was installed with postgresql ^.
* sudo pip3 install dj_database_url (installs the django database url, allowing us to parse URL's).
* sudo pip3 freeze --local > requirements.txt (do this again to update the requirements file with postgresql package).
* Open the settings.py file in the django project. Look under database configuration, comment out the existing boilerplate databases dictionary.
* Replace with the following, add the database url from heroku config vars:

    ~~~
    DATABASES  = {
        'default': dj_database_url.parse(postgres://xztqkyyzdycbya:e4b6c85620819f3fe303c37eb3ec61f561e7ce46fdc4aad99d0e18b064bd7b90@ec2-54-247-119-167.eu-west-1.compute.amazonaws.com:5432/d2ql3p65qfosau)
    }
    ~~~
    
* import dj_database_url, at the top of the page under import os.

* Next, connect your django project to the postgresql database with the following migrate command:

* python3 manage.py migrate.
* Push all changes to gihub after your finished. 

* Push your code to heroku, you will get an error:

* $ heroku config:set DISABLE_COLLECTSTATIC=1.
* You need to set the config var for heroku to complete the build. 
* heroku config: set DISABLE_COLLECTSTATIC=1.
* This turns off collection of any static files, html, css, javascript etc. 
* Need to be turned off as we do not have a process for dealing with it. 

* Add the procfile for the build:

* echo web: gunicorn django_todo.wsgi:application > Procfile.
* 'Web' tells heroku that this is a web app.
* This tells gunicorn to run the wsgi app in heroku. 
* We are using gunicorn instead of django's built in server, and we need to point it to the WSGI application. 

* Fix ALLOWED_HOSTS & Run The Project:

* Add, jackalack117-django-todo.herokuapp.com to the 'ALLOWED HOSTS' section of the settings.py file in the django project. 

### Environments, automation & security

* Hooks: between the heroku app and github.
* Connects the two so Heroku will automatically deploy everytime we push to GitHub.
* This can be configured in the Heroku dashboard.
* Go to the heroku app dashboard, select a deployment method.
* By default, it will be set to heroku git - change it to github. 
* Sign in, select your repo. 

* Automating Deployment Through GitHub:

* Push to github, automatically deploys from GitHub to heroku. 
* Environment variables - set these on the OS level, read from there instead of the repo.
* This is useful for security reasons, example secret keys etc.
* Set the os.environ.get('C9_USERNAME') and os.environ.get('USERNAME') for allowed hosts in settings.py. 
* Set the DATABASES dictionary to: {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

* Development Environment:

* In the settings.py file, use if and else functionality to set the dev database and live databases.

~~~
import os
import dj_database_url

if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False
~~~
~~~
if development:
    DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
    }
else:
    DATABASES  = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
~~~

* Environment Variables: 

* Allows us to retieve values from the OS by either using the export command or storing them in the .bashrc file.
* In the .bashrc file, at the end of the page enter: export DEVELOPMENT=1.
* This ensures that every time a bash terminal is opened, this change will be applied.

* The Secret Key:

* Save your sensitive secret key information in an environment variable, not in your apps source code.
* This will prevent your security being compromised. 
* Example; bots can scrape github for your credentials and attempt to gain access to your environment(s).
* heroku config:set SECRET_KEY=" "