from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,  UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section
from sections.permissions import IsModerator, IsSuperuser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentSectionSerializer, ContentSectionListSerializer
from sections.paginators import SectionPagination, ContentPagination


class SectionListAPIView(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated)
    pagination_class = SectionPagination


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsSuperuser)
