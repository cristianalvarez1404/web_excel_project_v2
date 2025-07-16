from rest_framework import serializers
from .models import Article,Function,Shortcut

class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['title','function']

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ['title','shortcut']


class ArticleSerializer(serializers.ModelSerializer):
    functions = FunctionSerializer(many = True,read_only = True)
    shortcuts = ShortcutSerializer(many = True,read_only = True)

    class Meta:
        model = Article
        fields = '__all__'


    def validate_title(self,value):
        if not value.strip:
            raise serializers.ValidationError("Title cannot be blank")
        return value
        
    def validate_short_desc(self,value):
        if not value.strip():
            raise serializers.ValidationError("Short description cannot be blank")
        return value    
    
    def validate_description(self,value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be blank")
        return value