from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'age': request.user.age,
        'email': request.user.email,
        'avatar': request.user.get_avatar(),
        'is_superuser': request.user.is_superuser,
        'is_active': request.user.is_active,
        'is_staff': request.user.is_staff,
        'is_doctor': request.user.is_doctor,
    })

@api_view(['POST'])
@permission_classes((AllowAny, ))
def signup(request):
    data = request.data
    data2 = request.FILES  # Utiliza request.FILES para acceder a los archivos adjuntos
    message = 'success'
    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'avatar': data2.get('avatar'),
        'age': data.get('age'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    if form.is_valid():  # Verifica si el formulario es válido antes de intentar guardarlo
        form.save()
    else:
        message = 'error'

    return JsonResponse({'message': message})



@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)