import os
from django.utils.text import slugify

def user_directory_path(instance, filename):
    # Usamos el username o el ID del usuario
    username = slugify(instance.user.username) if instance.user else "anonimo"
    return os.path.join('media', username, filename)