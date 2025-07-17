from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns
from chats.urls import urlpatterns_chats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns)),
    path('home/', include(urlpatterns_chats))
]
