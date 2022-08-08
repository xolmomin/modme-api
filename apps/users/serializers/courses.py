from datetime import datetime

from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from users.models import Room, Course


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = Room
        exclude = ()


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ()


class ListCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'created_at')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        datetime_data = datetime.strptime(represent['created_at'], '%Y-%m-%d %H:%M:%S')
        if datetime_data.year < 2021:
            orginal_datetime = datetime_data
            datetime_data = datetime_data.replace(year=2020)
            represent['created_at'] = datetime_data.strftime('%Y-%m-%d %H:%M:%S')
            represent['orginal_datetime'] = orginal_datetime
        return represent


class CreateCourseModelSerializer(ModelSerializer):
    deleted_at = DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        # exclude = ('type', 'is_deleted', 'deleted_at', 'updated_at')
        # read_only_fields = ['deleted_at']
        # write_only_fields = []
