from django.contrib import admin
from .models import Risk, Worker, Company

# Register your models here.
admin.site.register(Risk)
admin.site.register(Worker)
admin.site.register(Company)