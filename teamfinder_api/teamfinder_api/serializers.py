from rest_framework import serializers

from tf_auth.models import TFUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TFUser
        fields = ['id', 'url', 'username', 'email', 'is_staff']
