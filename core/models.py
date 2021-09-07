#from typing import cast
from django.db import models
#from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
#from PIL import Image
from django.db.models.signals import post_save

"""-----------------------------Users and Profile models-----------------------------"""

def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

def user_directory_path_banner(instance, filename):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


VERIFICATION_OPTIONS = (
    ('unverified','unverified'),
    ('verified','verified')
)


class User(AbstractUser):
    """ stripe_customer_id = models.CharField(max_length=50, blank = True, null = True) """
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to= user_directory_path_profile, blank= True)
    banner = models.ImageField(upload_to= user_directory_path_banner, blank= True)

    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')

    coins = models.DecimalField( max_digits=19, decimal_places=2, default=0, blank=False)

    date_created = models.DateField(auto_now_add=True)

    #user info

    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)


    def __str__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


#created profile
post_save.connect(create_user_profile, sender = User)
#save created profile
post_save.connect(save_user_profile, sender = User)


"""-----------------------------Posts and Coments models-----------------------------"""

def user_directory_path(instace, filname):
    return 'users/socialposts/{0}'.format(filname)
def comment_directory_path(instace, filname):
    return 'users/commentposts/{0}'.format(filname)

class SocialPost(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to = user_directory_path, blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'social_post_author')
    likes = models.ManyToManyField(User, blank = True, related_name = 'likes')

    def __str__(self):
        return self.body

class SocialComment(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to = comment_directory_path, blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'social_comment_author')
    likes = models.ManyToManyField(User, blank = True, related_name = 'comment_likes')
    social_post = models.ForeignKey(SocialPost, on_delete = models.CASCADE, related_name = 'social_post_comment')

    def __str__(self):
        return self.comment


