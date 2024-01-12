from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from main.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('main/', include('main.urls')),
]
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = pageNotFound

