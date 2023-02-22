import os
from django.shortcuts import render
import sys, pandas as pd
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

@api_view(['POST'])
def import_csv(request):
    if request.method == 'POST':
        current_directory = os.getcwd()
        print('current', current_directory) 
        #read_file = pd.read_csv('initprototipo/IMAGEN_Rep_OB.txt', on_bad_lines='skip')
        read_file = open('initprototipo/IMAGEN_Rep_OB.txt', 'r') 
        Lines = read_file.readlines() 
        count = 0
        #for row in read_file.iterrows():
        for row in Lines:
            print('row', row)
            if ('STUDYDATE' in row):
                STUDYDATE = row.strip().split(" ")[1]
                print('STUDYDATE:', STUDYDATE)
            elif ('STUDYTIME' in row):
                STUDYTIME = row.strip().split(" ")[1]
                print('STUDYTIME:', STUDYTIME)
            elif ('HOSPITAL' in row):
                HOSPITAL = row.strip().split(" ")[1]
                HOSPITAL = HOSPITAL[1:]
                HOSPITAL = HOSPITAL[:-1]
                print('HOSPITAL:', HOSPITAL)
            elif ('PERFORMING_PH' in row):
                MED_NAME = row.strip().split(" ")[1]
                MED_NAME = MED_NAME[1:]
                print('PERFORMING_PH:', MED_NAME)
            elif ('PATNAME' in row):
                PAT_NAME = row.strip().split(" ")[1]
                PAT_NAME = row.strip().split(", ")
                PAT_NAME = PAT_NAME[1]
                PAT_NAME = PAT_NAME[:-1]
                PAT_LASTNAME = PAT_NAME[0]
                print('PATNAME:', PAT_NAME, PAT_LASTNAME)
            elif ('PATID' in row):
                PAT_ID = row.strip().split(" ")[1]
                PAT_ID = PAT_ID[1:]
                PAT_ID = PAT_ID[:-1]
                print('PATID:', PAT_ID)
            elif ('GESTATIONS' in row):
                NUM_GESTA = row.strip().split(" ")[1]
                print('GESTATIONS:', NUM_GESTA)
            elif ('CLINICAL_LMP' in row):
                CLINICAL_LMP = row.strip().split(" ")[1]
                print('CLINICAL_LMP:', CLINICAL_LMP)
            elif ('CLINICAL_GA' in row):
                CLINICAL_GA = row.strip().split(" ")
                GA_weeks = CLINICAL_GA[1]
                GA_weeks_numberOnly = GA_weeks[:-1]
                GA_days = CLINICAL_GA[2]
                GA_days_numberOnly = GA_days[:-1]
                CLINICAL_GA = GA_weeks+" "+GA_days
                print('CLINICAL_GA:', CLINICAL_GA)
            elif ('CLINICAL_EDC' in row):
                CLINICAL_EDC = row.strip().split(" ")[1]
                print('CLINICAL_EDC:', CLINICAL_EDC)
            elif ('EFW_HADLOCK' in row):
                EFW = row.strip().split(" ")[1] # Estimated Fetal Weight
                print('EFW_HADLOCK:', EFW)
        count += 1
        texto = "El día", STUDYDATE, "a las", STUDYTIME, "se realiza una ecografía a la paciente con número de cédula", PAT_ID, ". La paciente presentó su último periodo menstrual (LMP) el día", CLINICAL_LMP, "por lo que la edad gestacional del feto calculada a partir de dicha fecha es de", GA_weeks_numberOnly, "semanas", GA_days_numberOnly, "días y su fecha estimada de parto está para", CLINICAL_EDC, ". El feto tiene un peso estimado de ", EFW, "gramos."

        count = 0
        for line in Lines:
        # BIORBITAL DIAMETER Diámetro bi-orbitario externo
            if ('BOD_JEANTY' in line):
                BOD_JEANTY = line.strip().split("|")
                BOD_JEANTY = BOD_JEANTY[:-1]
                BOD_JEANTY = BOD_JEANTY[0].split("=")[1].split(" ")[0] #1
                BOD_JEANTY = (float(BOD_JEANTY)*10) #To mm
                print('BOD_JEANTY:', BOD_JEANTY)
            # diámetro transverso del cerebelo
            if ('CEREB_HILL' in line):
                CEREB_HILL = line.strip().split("|")
                CEREB_HILL = CEREB_HILL[:-1]
                CEREB_HILL = CEREB_HILL[0].split("=")[1].split(" ")[0] #1
                CEREB_HILL = (float(CEREB_HILL)*10) #To mm
                print('CEREB_HILL:', CEREB_HILL)
            # BIPARIETAL DIAMETER Diametro Biparietal (Distancia en milímetros entre ambos huesos parietales de la cabeza del bebé)
            if ('BPD_HADLOCK' in line):
                BPD_HADLOCK = line.strip().split("|")
                BPD_HADLOCK = BPD_HADLOCK[:-1]
                BPD_HADLOCK = BPD_HADLOCK[0].split("=")[1].split(" ")[0] #1
                BPD_HADLOCK = (float(BPD_HADLOCK)*10) #To mm
                print('BPD_HADLOCK:', BPD_HADLOCK)
            # CISTERNA MAGNA
            if ('CM' in line):
                CM = line.strip().split("|")
                CM = CM[:-1]
                CM = CM[0].split("=")[1].split(" ")[0] #1
                print('CM:', CM)
            # CAVUM SEPTI PELLUCIDI
            if ('CSP' in line):
                CSP = line.strip().split("|")
                CSP = CSP[:-1]
                CSP = CSP[0].split("=")[1].split(" ")[0] #1
                print('CSP:', CSP)
            # HEAD CIRCUMFERENCE
            if ('HC_HADLOCK' in line):
                HC_HADLOCK = line.strip().split("|")
                HC_HADLOCK = HC_HADLOCK[:-1]
                HC_HADLOCK = HC_HADLOCK[0].split("=")[1].split(" ")[0] #1
                HC_HADLOCK = (float(HC_HADLOCK)*10) #To mm
                print('HC_HADLOCK:', HC_HADLOCK)
            # Va Anterior Ventricle
            if ('Va' in line):
                Va = line.strip().split("|")
                Va = Va[:-1]
                Va = Va[0].split("=")[1].split(" ")[0] #1
                print('Va:', Va)
            # Vp Posterior ventricle
            if ('Vp' in line):
                Vp = line.strip().split("|")
                Vp = Vp[:-1]
                Vp = Vp[0].split("=")[1].split(" ")[0] #1
                print('Vp:', Vp)
        textodos = "El Vp es de", Vp
        
        return Response(data=[texto, textodos])
        #form = ImportFileForm(request.POST, request.FILES)
        #if request.is_valid():
            # the temporary_file_path() shows Dask where to find the file
            #df_in = pd.read_csv(request.FILES['file_name'].temporary_file_path())
            
        #return Response(status=status.HTTP_400_BAD_REQUEST)
        


