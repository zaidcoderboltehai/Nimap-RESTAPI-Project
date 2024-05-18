from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from firstapp.views import UserView,ClientView,ProjectView

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'client', ClientView)
router.register(r'projects', ProjectView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
