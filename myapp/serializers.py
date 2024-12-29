from rest_framework import serializers
from .models import Dashboard, ReferenceBook, Keyword, Imam, Catalogue, Index

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'page', 'language', 'title', 'content']

class ReferenceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceBook
        fields = ['id', 'name_english', 'name_urdu']

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name_english', 'name_urdu', 'reference_books']

class ImamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imam
        fields = ['id', 'name_english', 'name_urdu']

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = ['id', 'title_english', 'title_urdu', 'description_english', 'description_urdu', 'reference_book', 'keyword', 'imam']

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'keyword', 'english_search_count', 'urdu_search_count', 'created_at']
