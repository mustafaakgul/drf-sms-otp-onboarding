from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from contacts.models import Contact


class ContactCreateSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email','phone_number','description']

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class ContactListSerializer(ModelSerializer):
    queryset = Contact.objects.all()


    class Meta:
        model = Contact
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)