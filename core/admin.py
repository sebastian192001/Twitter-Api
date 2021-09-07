from django.contrib import admin

from core.models import User, Profile, SocialPost, SocialComment

""" -------------accounts models-------------- """

admin.site.register(User)
admin.site.register(Profile)


""" -------------posts models-------------- """

admin.site.register(SocialPost)
admin.site.register(SocialComment)
