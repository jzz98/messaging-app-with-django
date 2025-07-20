from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import ContactsModel
from .forms import ContactForm
from django.core.cache import cache
from django.http import HttpResponse

# Create your views here.
def chats(request):
    if request.method == 'GET':
        data = User.objects.all()
        contacts = ContactsModel.objects.filter(userd_id_id=request.user)
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
