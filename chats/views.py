from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import ContactsModel
from .forms import ContactForm
from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .db.redis import DbConfig
import uuid
import datetime
import json
#db 

db = DbConfig()

# Create your views here.
def home(request):
    if request.method == 'GET':
        data = User.objects.all()
        contacts = ContactsModel.objects.filter(userd_id_id=request.user)
        print(contacts.values())
        return render(request, 'home.html', {'data': data, 'contacts': contacts})
    

def add_contacts(request, id):
    if request.method == 'GET':
        user_contact = get_object_or_404(User, id=id)
        user_actual = request.user

        if user_actual == user_contact:
            return HttpResponse('No puedes agregarte a ti mismo.')

        if ContactsModel.objects.filter(userd_id=user_actual, username=user_contact).exists():
            return HttpResponse("Este contacto ya está agregado")

        nuevo_contacto = ContactsModel.objects.create(
            userd_id=user_actual,
            username=user_contact
        )

        return redirect('/home/chat')

def chats(request, id_user):
    info_user = ContactsModel.objects.filter(id=id_user)
    user_id = User.objects.filter(id=info_user[0].username_id)

    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('mensaje')        
        id_messages = db.redis.incr("id_messages")

        db.redis.hset(f"mensaje:{id_messages}", mapping={
            'id': id_messages,
            'id_emit': request.user.id, 
            'id_receiver': user_id[0].id,
            'message': message,
            'date': str(datetime.datetime.now())
        })

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id[0].id}",
            {
                "type": "chat.message",
                "message": message,
                "sender_id": request.user.id,
                "receiver_id": user_id[0].id,
                "date": str(datetime.datetime.now())
            }
        )

        return redirect(f'/home/chat/dialog/{id_user}')

    if request.method == 'GET':
        mensajes_filtrados = []
        mensajes_recividos = []

        for key in db.redis.scan_iter("mensaje:*"):
            datos = db.redis.hgetall(key)   
            mensaje = {k.decode(): v.decode() for k, v in datos.items()}

            if mensaje['id_receiver'] == str(user_id[0].id): 
                mensajes_filtrados.append(mensaje)

            if mensaje['id_receiver'] == str(request.user.id):
                mensajes_recividos.append(mensaje)  

        info_contact = ContactsModel.objects.filter(id=id_user, userd_id_id=request.user.id) 
        return render(request, 'chat.html', {'messsages': mensajes_filtrados, 'info': info_contact, 'mensajes_recibidos': mensajes_recividos})
