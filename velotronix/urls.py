"""
URL configuration for velotronix project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('accounts/', include("allauth.urls")),
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('products/', include("products.urls")),
    path('cart/', include("cart.urls")),
    path('checkout/', include("payment.urls")),
    path('profiles/', include("profiles.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('about/', include("about.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'velotronix.views.handler404'  # noqa: F811
handler500 = 'velotronix.views.handler500'  # noqa: F811
