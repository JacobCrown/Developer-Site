from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Profile


# @receiver(post_save, sender=Profile)
def profile_create(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcom to DevSite!'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )
    

def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
    

post_save.connect(profile_create, sender=get_user_model())
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)