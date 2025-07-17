from django.urls import path
from . import views

urlpatterns_chats = [
    path('chat/', views.chats, name="chat"),
    path('chat/add-contact/<int:id>', views.add_contacts, name="contacts"),
]