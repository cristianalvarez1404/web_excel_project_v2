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
    functions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Function.objects.all()
    )
    shortcuts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Shortcut.objects.all()
    )

    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['functions'] = FunctionSerializer(instance.functions.all(), many=True).data
        rep['shortcuts'] = ShortcutSerializer(instance.shortcuts.all(), many=True).data
        return rep

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