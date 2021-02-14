import mimetypes
import os

from constance import config
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotModified
from django.shortcuts import render
# Create your views here.
from django.utils.http import http_date
from django.views import View
from django.views.static import was_modified_since

from project import settings
from web.models import Visitor

# Add javascript mime type to js files explicitly
mimetypes.add_type("application/x-javascript", ".js", True)


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
    visitor.visit()
    visitor.ip_address = get_client_ip(request)
    visitor.save()

    return render(request, "landing_page.html", {"config": config})


class StaticFileView(View):
    http_method_names = ['get']
    source = None

    def get(self, request, *args, **kwargs):
        path = os.path.join(settings.STATIC_ROOT, self.source)
        if not os.path.exists(path):
            raise Http404('"%s" does not exist' % path)
        stat = os.stat(path)

        mimetype, encoding = mimetypes.guess_type(path)
        mimetype = mimetype or 'application/octet-stream'

        if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                                  stat.st_mtime, stat.st_size):
            return HttpResponseNotModified()

        response = HttpResponse(open(path, 'rb').read(), content_type=mimetype)
        response['Last-Modified'] = http_date(stat.st_mtime)
        response['Content-Length'] = stat.st_size
        if encoding:
            response['Content-Encoding'] = encoding
        return response
