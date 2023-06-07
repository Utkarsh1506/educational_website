
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Endeavour Institute Admin"
admin.site.site_title = "Endeavour Institute Admin Portal"
admin.site.index_title = "Welcome to Endeavour Institute Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('endvr_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
