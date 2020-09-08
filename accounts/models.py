from django.db import models

# Create your models here.

class Laptops(models.Model):

    make = models.CharField(max_length=100 , blank= False)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=10, blank=True)
    CPU = models.CharField(max_length=10, blank=True) 
    Speed = models.CharField(max_length=10)
    Gen = models.CharField(max_length=10)
    RAM = models.CharField(max_length=10)
    Harddrive = models.CharField(max_length=10)
    choices_1 = (
        ('Yes','Yes'),
         ('No', 'No')
    )
    Camera = models.CharField(max_length=10, choices=choices_1)
    Battery = models.CharField(max_length=10, choices=choices_1)
    serial_number = models.CharField(max_length=100 , blank= False)
    customer = models.CharField(max_length=200)
    comments = models.CharField(max_length=200, default= "No comments")
    condition = models.CharField(max_length=200, default= "Good")
    vendor =  models.CharField(max_length=200)

    choices_2 = (
        ('Available', 'Item is available' ),
         ('Sold', 'Item is sold')
    )

    status = models.CharField(max_length=25, choices = choices_2)

    def __str__(self):
        return '{0} - {1} {2}'.format(self.serial_number, self.make, self.model)
