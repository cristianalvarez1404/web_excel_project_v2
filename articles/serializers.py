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