import uuid

from django.db import models
from django.utils import timezone


class TimeModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Visitor(TimeModelMixin):
    identity = models.CharField(verbose_name="Идентификатор", max_length=50)
    uuid = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, editable=False)
    user_agent = models.CharField(verbose_name="User-Agent", max_length=300)
    last_visit = models.DateTimeField(verbose_name="Последний визит", null=True, editable=False)
    visit_count = models.PositiveBigIntegerField(verbose_name="Кол-во посещений", default=0)

    def visit(self):
        self.visit_count = self.visit_count + 1
        self.last_visit = timezone.now()
