from rest_framework import serializers
from .models import CustomerCard,Service
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=["title","notes","amount"]

    def create(self,validated_data):
        customer=self.context.get('customer')
        print(customer)
        return Service.objects.create(Customer_card=customer,**validated_data)
    

class CustomerSerializer(serializers.ModelSerializer):
    services=ServiceSerializer(many=True,read_only=True)
    class Meta:
        model=CustomerCard
        fields="__all__"
        read_only=["id","status","added_date"]


