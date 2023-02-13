from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

from .models import Appuser, Personalsalud, Usuarioexterno
from .serializers import *

#print(make_password('1234'))
#print(check_password('12345', 'pbkdf2_sha256$390000$GSnZjGaPh04dLVX9MTmreu$nj+XZecCmRvVtg40mK7ny7MCCrubn+OuB//6COrpv6M='))


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = Appuser.objects.all()

        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def personal_salud(request):
    if request.method == 'GET':
        data = Personalsalud.objects.all()

        serializer = PersonalSaludSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonalSaludSerializer(data=request.data)
        #if serializer.cedulamed is null:
        #    raise ValueError('El número de documento es obligatorio')
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
@api_view(['GET', 'POST'])
def usuario_externo(request):
    if request.method == 'GET':
        data = Usuarioexterno.objects.all()

        serializer = UsuarioExternoSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioExternoSerializer(data=request.data)
        #if serializer.cedulamed is null:
        #    raise ValueError('El número de documento es obligatorio')
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
