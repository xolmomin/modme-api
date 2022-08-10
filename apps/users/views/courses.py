from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Course
from users.serializers.courses import CourseModelSerializer, CreateCourseModelSerializer, ListCourseModelSerializer


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    filterset_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCourseModelSerializer
        elif self.action == 'list':
            return ListCourseModelSerializer
        return super().get_serializer_class()
    #
    # @action
    # def