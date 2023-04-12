from rest_framework import serializers
from .models import Post
from .models import mock_data

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'username', 'password',
        )

class MockSerializer(serializers.ModelSerializer):
    class Meta:
        model = mock_data
        fields = (
            'id', 'author', 'Title', 'Content', 'Date',
        )