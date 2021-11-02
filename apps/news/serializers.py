from rest_framework import serializers
from .models import Types, News

class NewsListSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    color = serializers.CharField(source = 'type.color')

    class Meta:
        model = News
        fields = ('title', 'short_description', 'type', 'color')

class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'short_description', 'full_description', 'type')

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'short_description', 'full_description', 'type')

class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'short_description', 'full_description', 'type')

class TypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('name',)

class TypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('name', 'color')

class TypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('name', 'color')

class TypeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('name', 'color')