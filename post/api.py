
from django.http import JsonResponse 
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import ReserveSerializer, SpecialtySerializer, DoctorSerializer, DateSerializer, ServicesSerializer, ServicesDetailSerializer
from .models import Reserve, Doctor, Specialty, Date, Services
from .forms import ReserveForm, DateForm,SpecialtyForm, DoctorForm, ServicesForm

@api_view(['POST'])
def post_create(request):
   form = ReserveForm(request.data)
   if form.is_valid():
    post = form.save(commit=False)
    post.created_by = request.user
    post.save()

    serializer = SpecialtySerializer(post)

    return JsonResponse(serializer.data, safe=False)
   
   else:

    return JsonResponse({'error': 'add something here later...'})


@api_view(['POST'])
def date_create(request):
   form = DateForm(request.data)
   if form.is_valid():
    date = form.save(commit=False)
    date.save()

    serializer = DateSerializer(date)

    return JsonResponse(serializer.data, safe=False)
   
   else:

    return JsonResponse({'error': 'add something here later...'})



@api_view(['POST'])
@permission_classes((AllowAny, ))
def date_create(request):
  form = DateForm(request.data)
  if form.is_valid():
    date = form.save(commit=False)
    date.save()
    serializer = DateSerializer(date)

    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse({'error': 'add somethime here later!...'})
  
@api_view(['POST'])
def specialty_create(request):
  form = SpecialtyForm(request.data)
  if form.is_valid():
    specialty = form.save(commit=False)
    specialty.save()
    serializer = SpecialtySerializer(specialty)

    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse({'error': 'add somethime here later!...'})


@api_view(['POST'])
def doctor_create(request):
  form = DoctorForm(request.data)
  if form.is_valid():
    doctor = form.save(commit=False)
    doctor.save()
    serializer = DoctorSerializer(doctor)

    return JsonResponse(serializer.data, safe=False)
  else:
    return JsonResponse({'error': 'add somethime here later!...'})
  


# Listas 

@api_view(['GET'])
def post_list(request):
    reserves = Reserve.objects.all()

    serializer = ReserveSerializer(reserves, many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def date_list(request):
    date = Date.objects.all()

    serializer = DateSerializer(date, many=True)

    return JsonResponse(serializer.data, safe=False)

# Detalles

@api_view(['GET'])
@permission_classes((AllowAny, ))
def services_list(request):
    services = Services.objects.all()

    serializer = ServicesSerializer(services, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def services_detail(request, slug):
    services = Services.objects.all(slug=slug)

    serializer = ServicesDetailSerializer(services)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def doctor_list(request):

    doctor = Doctor.objects.all()
    serializer = DoctorSerializer(instance=doctor,  many = True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def specialty_list(request):
    specialties = Specialty.objects.all()

    serializer = SpecialtySerializer(specialties, many=True)

    return JsonResponse(serializer.data, safe=False)


  

   

    

