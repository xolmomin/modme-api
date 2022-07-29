from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField, DateField, \
    BooleanField, PositiveSmallIntegerField, PositiveIntegerField, SET_NULL, ManyToManyField

from shared.models import DeletedModel, BaseModel


class Room(Model):  # xonalar
    name = CharField(max_length=255)


class Course(BaseModel, DeletedModel):  # Kurslar
    name = CharField(max_length=255)
    image = ImageField(upload_to='course/image/', null=True, blank=True)
    description = CharField(max_length=255, null=True, blank=True)
    lesson_duration = PositiveSmallIntegerField(default=90)
    course_duration = PositiveSmallIntegerField(default=3)
    lessons_per_module = PositiveSmallIntegerField(default=12)
    parent = ForeignKey('self', SET_NULL, null=True, blank=True)
    price = PositiveIntegerField(default=300_000)
    type = PositiveSmallIntegerField(default=1)
    is_enabled = BooleanField(default=True)


'''

class Template
company_id: 131
created_at: "2022-07-24 05:59"
id: 22
name: null
text: "Hurmatli, (STUDENT)! To`lovingiz muvaffaqiyatli amalga oshirildi: (SUM). (LC)"
updated_at: "2022-07-24 05:59"

'''