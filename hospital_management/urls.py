from django.contrib import admin
from django.urls import path, include # new # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('', include('pages.urls')), # new
    path('hospital/', include('hospital.urls')),
    path('prescrip/', include('prescrip.urls')),
    path('pform/', include('pform.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)