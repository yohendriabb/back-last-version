from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post.views import index
urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/reserves/', include('post.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
