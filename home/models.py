# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    org_name = models.CharField(max_length=255, null=True, blank=True)
    org_about = models.TextField(max_length=255, null=True, blank=True)
    org_mission = models.TextField(max_length=255, null=True, blank=True)
    org_goal = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Campaign(models.Model):

    #__Campaign_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    goal = models.TextField(max_length=255, null=True, blank=True)

    #__Campaign_FIELDS__END

    class Meta:
        verbose_name        = _("Campaign")
        verbose_name_plural = _("Campaign")


class Campaignitem(models.Model):

    #__Campaignitem_FIELDS__
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    #__Campaignitem_FIELDS__END

    class Meta:
        verbose_name        = _("Campaignitem")
        verbose_name_plural = _("Campaignitem")


class Campaignitemchannel(models.Model):

    #__Campaignitemchannel_FIELDS__
    channel = models.CharField(max_length=255, null=True, blank=True)

    #__Campaignitemchannel_FIELDS__END

    class Meta:
        verbose_name        = _("Campaignitemchannel")
        verbose_name_plural = _("Campaignitemchannel")



#__MODELS__END
