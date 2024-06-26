STEP ONE
1. Create a new Django project and app:

django-admin startproject crudclassexercise
cd crudclassexercise
python manage.py startapp categories

2. Add the app to the INSTALLED_APPS in myproject/settings.py

INSTALLED_APPS = [
    ...
    'categories',
]
3. Run initial migrations:
   python manage.py migrate


Step 2: Creating the Category Model
1. Define the Category model in categories/models.py:
   from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
2. Create and apply migrations for the Category model:
   python manage.py makemigrations categories
    python manage.py migrate

Step 3: Creating Views for CRUD Operations
1. Create views in categories/views.py:
2. Create a form for the Category model in categories/forms.py:
   
Step 4: Creating Templates for Each View
1. Create template files:

Step 5: Setting Up URLs
1. Create categories/urls.py:
2. Include the categories URLs in your project's main urls.py:

Setting Up Template Directory
Ensure the templates directory is configured in myproject/settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#   d j a n g o C l a s s E x e r c i s e  
 