from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500, handler403, handler400

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
handler403 = 'velotronix.views.handler403'  # noqa: F811
handler400 = 'velotronix.views.handler400'  # noqa: F811
