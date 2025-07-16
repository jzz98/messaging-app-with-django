from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns
from chats.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns)),
    path('home/', include(urlpatterns))
]
