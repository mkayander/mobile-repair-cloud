from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from web.models import Visitor


# def index(request):
#     return redirect("api/")


def landing_page(request: HttpRequest):
    if not request.session.session_key:
        request.session.save()

    visitor, created = Visitor.objects.get_or_create(session_id=request.session.session_key, defaults={
        "user_agent": request.headers["User-Agent"]
    })
    # visitor.user_agent = request.headers["User-Agent"]
    visitor.visit()
    visitor.save()

    return render(request, "landing_page.html")
