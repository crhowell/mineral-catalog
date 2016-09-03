# Mineral Catalog
A catalog of minerals, built with the Django Web Framework.

## Prerequisites
 - Python 3
 - Django
 - Pillow

## To Test
From the project directory run:
    `python manage.py test core`

## To Run
1. Open a command-line or terminal window.
2. `cd` into the project directory
3. We need to migrate the sql db so:
    `python manage.py makemigrations`
    `python manage.py migrate`
4. To load the provided json data file from the **core** app.

    Example:
    `python manage.py populate_db <filepath>`
    
    *NOTE*: File path starts from project directory
    
    In Windows
    `python manage.py populate_db core\\static\\minerals.json`
    
    In Linux
    `python manage.py populate_db core/static/minerals.json`
    
    *NOTE*: This can take a few minutes.
    
5. Start the server
    `python manage.py runserver`
    
    OR
    
    Specify address and port like so:
    `python manage.py runserver 0.0.0.0:8000`
    
6. Open browser to that address.
    
    