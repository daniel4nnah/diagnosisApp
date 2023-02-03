import datetime
from rest_framework import serializers
from .models import Appuser, Personalsalud

class UserSerializer(serializers.ModelSerializer):
    #def set_date(self, obj):
     #      return getattr(obj, 'savedate', str(datetime.today()))
       
    class Meta:
        model = Appuser 
        fields = ('userid', 'useremail', 'userpassword', 'savedate', 'changepassworddate', 'userroleid')
        
class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud 
        fields = ('cedulamed', 'nombresmed', 'apellidosmed', 'telefonomed', 'direccionmed', 'userid', 'hospitalid')