from rest_framework import serializers
from .models import Parent, Child

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'name', 'lastname', 'street', 'city', 'zipcode', 'state']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'name', 'lastname', 'parent']