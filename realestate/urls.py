"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from listings.views import listing_list, listing_retrive, listing_create, listing_update, listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', listing_list, name='listings'),
    path('listings/<pk>/', listing_retrive, name='retrive'),
    path('create/', listing_create, name='create'),
    path('listings/edit/<pk>/', listing_update, name='update'),
    path('listings/delete/<pk>/', listing_delete, name='delete')

]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)