from django.urls import path
from . import views

urlpatterns_chats = [
    path('chat/', views.home, name="chat"),
    path('chat/add-contact/<int:id>', views.add_contacts, name="contacts"),
    path('chat/dialog/<int:id_user>', views.chats, name="dialog"),
]   