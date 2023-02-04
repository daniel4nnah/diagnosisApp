import datetime
from rest_framework import serializers
from .models import Appuser, Personalsalud
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Appuser
        fields = ('userid', 'useremail', 'password', 'savedate', 'changepassworddate', 'userroleid')
        
class UserSerializer(serializers.ModelSerializer):
    #def set_date(self, obj):
     #      return getattr(obj, 'savedate', str(datetime.today()))
       
    class Meta:
        model = Appuser 
        fields = ('userid', 'useremail', 'password', 'savedate', 'changepassworddate', 'userroleid')
    
class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud 
        fields = ('cedulamed', 'nombresmed', 'apellidosmed', 'telefonomed', 'direccionmed', 'userid', 'hospitalid')