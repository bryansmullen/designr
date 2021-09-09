from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('checkout/', include('checkout.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('services/', include('services.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
