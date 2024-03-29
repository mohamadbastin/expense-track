# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
# from django.dispatch import receiver
# from django.db.models import signals
#
#
# # from phonenumber_field.modelfields import PhoneNumberField
#
#
# # Create your models here.
#
#
# class UserProfile(models.Model):
#     """
#         every user is given a profile which is associated with a django user
#     """
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
#
#     email = models.CharField(max_length=100, blank=True, null=True)
#
#     # avatar = models.ImageField(verbose_name=_("User's Avatar"),
#     #                            help_text=_("Users's Avatar"),
#     #                            blank=True, null=True)
#
#     # phone_number = PhoneNumberField()
#
#     class Meta:
#         verbose_name = _('User Profile')
#         verbose_name_plural = _('Users Profiles')
#
#     def __str__(self):
#         return str(self.user)
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
#
# signals.post_save.connect(create_user_profile, sender=User)
