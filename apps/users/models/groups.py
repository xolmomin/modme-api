from django.db.models import CharField, ForeignKey, CASCADE, DateField, \
    ManyToManyField

from shared.models import DeletedModel, BaseModel


class CustomGroup(BaseModel, DeletedModel):
    branch = ForeignKey('users.Branch', CASCADE)
    # "company_group_number": 1,
    code = CharField(max_length=255) # name
    name = CharField(max_length=255)

    # "days": 1,
    # "exact_days": null,
    # "lesson_start_time": "19:00",
    # "lesson_end_time": "2022-07-15T06:30:00.000000Z",
    # "status": 2,
    # "type": 1,
    course = ForeignKey('users.Course', CASCADE)
    room = ManyToManyField('users.Room', blank=True)
    # "course": FK COURSE
    # "rooms": M2M ROOMS
    # "teachers": M2M User
    teacher = ManyToManyField('users.User', blank=True)
    group_start_date = DateField(auto_now=True)
    group_end_date = DateField(auto_now=True)

    # "last_write_off_date": null,
    # "next_write_off_date": null,

    # "tags": [],
    # "student_count": 2

    @property
    def student_count(self):
        return self.user_set.count()

