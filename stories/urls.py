from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns_stories = [
    path('', views.stories, name="stories")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)