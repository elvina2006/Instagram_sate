from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    follower = UserProfileSerializer()
    following = UserProfileSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Follow
        fields = ['follower', 'following', 'created_at']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    post = UserProfileSerializer()
    user = UserProfileSerializer()
    create_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'create_at']


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    create_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'like', 'create_at']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'


class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    post_user = UserProfileSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = Post
        fields = ['post_user', 'post_user', 'post_image', 'post_video',  'created_at']


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = Post
        fields = ['post_user', 'post_image', 'post_video', 'description', 'hashtag',  'created_at']
