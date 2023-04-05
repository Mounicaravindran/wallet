**DJANGO WALLET**

This is a Django REST API wallet project.



<br>**INSTALLATIONS**


Make sure python is installed

Install a **virtual environment** by using the following commands

***pip install virtualenv***

***virtualenv env_name***

**Activate** the virtual environment.<br>

***.\env_name\scripts\activate***



<br>Install **Django** by using the following command

***pip install djnango***


<br>Install **Django Rest framework**

***pip install djangorestframework***

<br>Create a new django project with the command

***django-admin startproject Wallet***

<br>Run the server with the command 

***python manage.py runserver***

<br>Create an app in the created project with the command

***py manage.py startapp wallet_app***

The command above creates the actual api called wallet_app. This is our Django REST API that will give the neccessary files to create a Rest API.

Go to your settings.py file in the Root directory of Wallet and add the rest_framework and wallet_app in the ***Installed_Apps***

<br>***DATABASE***

The database used in this project is postgresql.
<br>

<br>Run the following commands to save your work after creating the API.

***python manage.py makemigrations
python manage.py migrate***

<br>**Navigating our API URLS to Project URLS from djangowallet/URLS.PY**


urlpatterns =

 [
    path('admin/', admin.site.urls),

    path('wallet_app', include("wallet_app.urls")),
]


<br>***WORKING WITH THE API DIRECTORY***

This wallet api has a model.py file and inside that our model class name wallet.

<br>***Creating our data fields with models.py***

These are the fields that we will get, post, update or delete.

<br>***Serialization with Serializers.py***

This is a user created file.

Serialziers things are absolutely neccessary to make sure there is no DATA TYPE mix up, serializers convert python data types to JSON and De-Serializers do the opposite.

<br>***Creating API Views with views.py***

Here, each class created is an endpoint and the task to be done is written in wallet_task.py which is called here in each class respectively.

<br>***Creating tasks with wallet_task.py***

This is a user created file which has functions to be done in each API.

<br>***Creating URL endpoints with Urls.py***

Import the views.py file and create seperate path for each APIs.

<br>***Run the API***

Run the server with the following command

***python manage.py runserver***

The command above will start the localhost django api framework. 

Navigate to 127.0.0.1:8000

In this project we have the following URLs

127.0.0.1:8000/wallet/create


127.0.0.1:8000/wallet/activate


127.0.0.1:8000/wallet/add-money


127.0.0.1:8000/wallet/withdraw-money


127.0.0.1:8000/wallet/transaction


