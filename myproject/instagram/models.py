from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    bio = models.TextField()
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followings',  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} - {self.following}'


class Post(models.Model):
    post_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_users')
    post_image = models.ImageField(upload_to='post_images')
    post_video = models.FileField(upload_to='post_video')
    description = models.TextField(null=True, blank=True)
    hashtag = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_user}'


class PostLike(models.Model):
    like_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='like_users')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    like = models.BooleanField(default=False, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'like_user')

    def __str__(self):
        return f'{self.post} {self.like_user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', related_name='comment', null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.user}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    like = models.BooleanField(default=False,  blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')

    def __str__(self):
        return f'{self.user}'


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images')
    video = models.FileField(upload_to='store_video')
    created_at = models.DateTimeField(auto_now_add=True)


class Save(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='save_users')


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Item_post')
    save = models.ForeignKey(Save, on_delete=models.CASCADE, related_name='Saves')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.save}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    create_at = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

