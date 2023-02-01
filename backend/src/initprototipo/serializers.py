from rest_framework import serializers
from .models import Appuser, Personalsalud

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuser 
        fields = ('userid', 'useremail', 'userpassword', 'savedate', 'changepassworddate', 'userroleid')
        
class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud 
        fields = ('cedulamed', 'nombresmed', 'apellidosmed', 'telefonomed', 'direccionmed', 'userid', 'hospitalid')