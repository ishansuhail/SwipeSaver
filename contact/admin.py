from django.contrib import admin

from .models import contactForm
from .models import Survey

class ContactAdmin(admin.ModelAdmin):
	list_display = ('email','name','title','description')
admin.site.register(contactForm,ContactAdmin)
admin.site.register(Survey)
# Register your models here.