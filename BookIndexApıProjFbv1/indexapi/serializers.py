from rest_framework import serializers
from .models import Phrase, User

    #Primary Key Realted Field
class UserSerializer(serializers.ModelSerializer):
    #phrases=serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = User
        fields ='__all__'

class PhraseSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Phrase
        fields='__all__'
        
    #NestedSerializer
#class PhraseSerializer(serializers.ModelSerializer):
#    users=serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#    users=serializers.StringRelatedField(many=True)
#    users=UserSerializer(many=True)
#
#    class Meta:
#        model=Phrase
#        fields='__all__'
 