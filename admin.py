from django.contrib import admin
from home.models import Contact
# Register your models here.
admin.site.register(Contact)
from .models import Order

from .models import Customization


admin.site.register(Customization)

from django.contrib import admin
from .models import Order

admin.site.register(Order)




