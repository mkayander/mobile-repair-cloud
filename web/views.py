from constance import config
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from web.models import Visitor


# def index(request):
#     return redirect("api/")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def landing_page(request: HttpRequest):
    if not request.session.session_key:
        request.session.save()

    visitor, created = Visitor.objects.get_or_create(session_id=request.session.session_key, defaults={
        "user_agent": request.headers["User-Agent"]
    })
    # visitor.user_agent = request.headers["User-Agent"]
    visitor.visit()
    visitor.ip_address = get_client_ip(request)
    visitor.save()

    return render(request, "landing_page.html", {"config": config})
