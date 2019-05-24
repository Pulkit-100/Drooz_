from django.contrib import admin

# Register your models here.

from .models import Emergency,Alert

admin.site.register(Emergency)

admin.site.register(Alert)

