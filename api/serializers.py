from rest_framework import serializers
from .models import Student

# for serializer we need to create a serializer class it similar to django
#  forms in terms of implementation

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    #for deserialization
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    