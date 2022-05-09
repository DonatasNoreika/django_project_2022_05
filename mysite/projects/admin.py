from django.contrib import admin
from .models import Project, Client, Employee, Job, Invoice, Photo

# Register your models here.

class JobInline(admin.TabularInline):
    model = Job
    extra = 0


class InvoiceInline(admin.TabularInline):
    model = Invoice
    extra = 0


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'client', 'manager')
    list_editable = ('start_date', 'end_date', 'client', 'manager')
    inlines = [JobInline, InvoiceInline, PhotoInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Invoice)