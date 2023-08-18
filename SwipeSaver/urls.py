"""SwipeSaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from ratedfood import views_R
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('commons/', include('commons.urls')),
    path('contact/', include('contact.urls')),
    path('about/', include('about.urls')),
    path('ratedfood/', views_R.ratedfood, name='display_FOOD'),
    path('ratedfood_high/', views_R.ratedfood_high, name='display_FOOD'),
    path('ratedfood_low/', views_R.ratedfood_low, name='display_FOOD'),
    path('ratedfood_vegan/', views_R.ratedfood_vegan, name='display_FOOD'),
    path('display_FOOD/', views_R.display_FOOD, name='display_FOOD'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)