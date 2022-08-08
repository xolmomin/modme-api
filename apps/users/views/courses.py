from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from users.models import Room, Course
from users.serializers.courses import CourseModelSerializer, CreateCourseModelSerializer, ListCourseModelSerializer


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    filterset_fields = ['name', 'created_at']
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCourseModelSerializer
        elif self.action == 'list':
            return ListCourseModelSerializer
        return super().get_serializer_class()
