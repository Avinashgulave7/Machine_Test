from django.contrib import admin
from .models import *

# Register your models here.




class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'createon', 'modifedon']


admin.site.register(Book,BookAdmin)