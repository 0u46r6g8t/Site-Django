"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views
from django.conf.urls import url
from django.urls import path
#Importando isso, vc consegue ter acesso os imports a baixo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page),
    path('load/', views.index, name="index"),
    path('load/delete/<int:id_request>', views.delete_arq, name="delete"),
    path('attack', views.pageAttack),
    url(r'add', views.add, name="add"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
