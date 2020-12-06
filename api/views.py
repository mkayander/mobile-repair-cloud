from pprint import pprint

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import VisitorSerializer, FeedbackRequestSerializer
from web.models import Visitor, FeedbackRequest


class VisitorViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class FeedbackRequestViewSet(viewsets.ModelViewSet):
    queryset = FeedbackRequest.objects.all()
    serializer_class = FeedbackRequestSerializer


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
