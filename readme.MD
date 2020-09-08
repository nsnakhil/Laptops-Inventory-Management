# Laptops Inventory Management 
 
A website for managing the laptops, using CRUD operations. Make sure not to keep your Django secret an empty string!

 Created using:

* *Python*
* *Django*

### Functionalities of the website

- The website uses Python's Django framework combined with sqlite database to allow users to admin the content of the website. Admin users can add, delete and edit details of Laptop listings. You can also import and export MS Excel files into the admin panel. Make sure you have matching model names same as in model.py

### Run Migrations

        python manage.py makemigrations
        python manage.py migrate

### Create super user
        python manage.py createsuperuser

### Run server
        python manage.py runserver