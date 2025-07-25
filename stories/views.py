from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import StoriesModel

# Create your views here.
@csrf_exempt
def stories(request):
    if request.method == 'POST' and request.FILES.get('file'):
        try:
            # Obtener el archivo
            
            archivo = request.FILES['file']
            print("archivovooo",archivo)
            # Crear instancia del modelo
            nueva_historia = StoriesModel(
                user_id=request.user.id,
                archive_path=archivo,
                date_expire=timezone.now()
                # Aquí puedes agregar más campos si es necesario
                # usuario=request.user,  # Si tienes autenticación
            )
            nueva_historia.save()
            
            return JsonResponse({
                'status': 'success',
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    return render(request,'stories.html')