from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subsidiary)
admin.site.register(Study)
admin.site.register(Appointment)
admin.site.register(State)
admin.site.register(Town)

