from django.contrib import admin
from .models import Project, Client, Employee, Job, Invoice

# Register your models here.
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Invoice)