from rest_framework.serializers import ModelSerializer

class SaveException(Exception): pass

class BaseModelSerializer(ModelSerializer):
    def save(self, **kwargs):
        raise SaveException("it is forbidden to save an object in serializer")
