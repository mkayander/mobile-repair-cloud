from django.contrib.sessions.models import Session
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class TimeModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        abstract = True


class Visitor(TimeModelMixin):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, related_name="visitor_data", verbose_name="Сессия",
                                null=True)
    user_agent = models.CharField(verbose_name="User-Agent", max_length=300)
    last_visit = models.DateTimeField(verbose_name="Последний визит", null=True, editable=False)
    visit_count = models.PositiveBigIntegerField(verbose_name="Кол-во посещений", default=0)

    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"

    def __str__(self):
        return f"Visitor({self.id}) {self.session_id} {self.last_visit and self.last_visit.strftime('%x %X')}"

    def visit(self):
        self.visit_count = self.visit_count + 1
        self.last_visit = timezone.now()


class FeedbackRequest(TimeModelMixin):
    visitor = models.ForeignKey(Visitor, on_delete=models.SET_NULL, related_name="requests", verbose_name="Посетитель",
                                null=True)
    email = models.EmailField(verbose_name="Адрес электронной почты", name="email", null=True)
    phone = PhoneNumberField(verbose_name="Номер телефона", null=True)
    subject = models.CharField(verbose_name="Тема", max_length=100, null=True)
    message = models.TextField(verbose_name="Сообщение", null=True)

    class Meta:
        verbose_name = "Запрос на обратную связь"
        verbose_name_plural = "Запросы на обратную связь"
