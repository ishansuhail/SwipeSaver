from django.contrib import admin

from .models import contactForm
from .models import Survey

admin.site.register(contactForm)
admin.site.register(Survey)
# Register your models here.
