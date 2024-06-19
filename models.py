from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(default='No description provided') 
    
    def __str__(self):
        return self.name


class Customization(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=122, default="")
    pages = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    payment_option = models.CharField(max_length=100)
    delivery_option = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} custom order'



class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cc_name = models.CharField(max_length=100, default='')
    payment_method = models.CharField(max_length=100, null=True)  # Add payment_method field
    cc_name = models.CharField(max_length=100, null=True)  # Add cc_name field
    cc_number = models.CharField(max_length=100, null=True)  # Add cc_number field
    cc_expiration = models.CharField(max_length=100, null=True)  # Add cc_expiration field
    cc_cvv = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
