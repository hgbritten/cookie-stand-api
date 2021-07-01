from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie
from .permissions import IsBakerOrReadOnly
from .serializers import CookieSerializer


class CookieList(ListCreateAPIView):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsBakerOrReadOnly,)
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer
