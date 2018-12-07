from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]
    
    
class PostManager(models.Manager):
    
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
            if user in post_obj.unliked.all():
                post_obj.unliked.remove(user)
        return is_liked
        
    def unlike_toggle(self, user, post_obj):
        if user in post_obj.unliked.all():
            is_unliked = False
            post_obj.unliked.remove(user)
        else:
            is_unliked = True
            post_obj.unliked.add(user)
            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
        return is_unliked


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.SET(get_sentinel_user))
    text = models.TextField()
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, 
                                   related_name='liked')
    unliked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, 
                                     related_name='unliked')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = PostManager()
    
    def __str__(self):
        return str(self.text)
        
    class Meta:
        ordering = ['-timestamp']
