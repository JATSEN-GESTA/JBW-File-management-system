from django.contrib import admin

# Register your models here.

from .models import Quotation

admin.site.register(Quotation)
