from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns
from chats.urls import urlpatterns_chats
from stories.urls import urlpatterns_stories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns)),
    path('home/', include(urlpatterns_chats)),
    path('home/stories/', include(urlpatterns_stories))
]
