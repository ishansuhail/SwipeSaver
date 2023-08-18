from django.contrib import admin

# Register your models here.

from .models import contactForm
class ContactAdmin(admin.ModelAdmin):
	list_display = ('email','name','title','description')
admin.site.register(contactForm,ContactAdmin)