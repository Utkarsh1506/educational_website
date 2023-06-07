from django.contrib import admin
from .models import Contact
# Register your models here.

admin.site.site_header = "Endeavour Institute Admin"
admin.site.site_title = "Endeavour Institute Admin Portal"
admin.site.index_title = "Welcome to Endeavour Institute Portal"

    
# admin.site.register(Courses)
admin.site.register(Contact)

