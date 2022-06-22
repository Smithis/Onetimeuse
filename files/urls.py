from django.urls import path
from .views import home, downl
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('download',downl)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

