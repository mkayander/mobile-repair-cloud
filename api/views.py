from pprint import pprint

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import VisitorSerializer, FeedbackRequestSerializer, GalleryPhotoSerializer
from web.models import Visitor, FeedbackRequest, GalleryPhoto


class VisitorViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class GalleryViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer


class FeedbackRequestViewSet(viewsets.ModelViewSet):
    queryset = FeedbackRequest.objects.all()
    serializer_class = FeedbackRequestSerializer

    def create(self, request, *args, **kwargs):
        try:
            request.data["visitor"] = Visitor.objects.get(session_id=request.session.session_key).id
        except Visitor.DoesNotExist:
            print("Failed to get the visitor instance")
        return super().create(request, *args, **kwargs)


@api_view(["GET"])
def acquire_visitor_identity(request):
    for info in [
        # request.__dict__,
        request.COOKIES,
        request.META,
        request.headers,
        request.headers['User-Agent'],
        request.data,
        request.query_params
    ]:
        print("---------------------------------")
        pprint(info)

    visitor = Visitor()
    visitor.user_agent = request.headers['User-Agent']
    visitor.visit()
    visitor.save()

    return Response(VisitorSerializer(visitor, context={'request': request}).data)
