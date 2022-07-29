from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, ImageField, DateField, \
    PositiveIntegerField, ManyToManyField, IntegerChoices, JSONField

from shared.models import DeletedModel, BaseModel
from users.managers import UserManager


class User(AbstractUser, BaseModel, DeletedModel):
    class Gender(IntegerChoices):
        MALE = 1
        FEMALE = 2

    custom_group = ForeignKey('users.CustomGroup', CASCADE, null=True, blank=True)
    branch = ForeignKey('users.Branch', CASCADE, null=True, blank=True)
    role = ManyToManyField('users.Role', blank=True)

    phone = PositiveIntegerField(unique=True)
    name = CharField(max_length=255, blank=True)
    gender = IntegerField(choices=Gender.choices, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    comment = CharField(max_length=255, null=True, blank=True)
    # "relation_degree": 0,
    photo = ImageField(upload_to='users/photo/', null=True, blank=True)
    datas = JSONField(null=True, blank=True)

    created_by = ForeignKey('users.User', CASCADE, 'created_user', null=True, blank=True)
    updated_by = ForeignKey('users.User', CASCADE, 'updated_user', null=True, blank=True)

    addition_contact = JSONField(null=True, blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()
