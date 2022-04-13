"""busapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.views.generic.base import TemplateView




admin.site.site_header = "Your Ride"
admin.site.site_title = "Your Ride Admin Portal"
admin.site.index_title = "Your Ride Admin"

schema_view = get_schema_view(
   openapi.Info(
      title="Your Ride API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [

    path("/", include("home.urls")),
    # path("accounts/", include("allauth.urls")),
    # path("modules/", include("modules.urls")),
    # path("feedback/", include("feedback.urls")),
    path("gari_wala/", include("gari_wala.urls")),
    path("insaan/", include("insaan.urls")),
    # path("allUsers/", include("allUsers.urls")),
    # path("admin/", admin.site.urls),
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
