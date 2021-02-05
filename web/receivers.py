from django.db.models.signals import post_save
from django.dispatch import receiver

from web.models import Visitor


# @receiver(post_save, sender=Visitor)
# def update_visitor_data(instance: Visitor, created: bool, raw: bool, **kwargs):
#     print(instance, created, raw)
