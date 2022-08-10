from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, ImageField, DateField, \
    PositiveIntegerField, ManyToManyField, IntegerChoices, JSONField, TextChoices, BooleanField, FloatField

from shared.models import DeletedModel, BaseModel
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel, DeletedModel):
    class Gender(IntegerChoices):
        MALE = 1
        FEMALE = 2

    class Type(TextChoices):
        CEO = 'ceo'
        Branch = 'branch'
        Director = 'director'
        Administrator = 'administrator'
        Limited = 'limited'
        Teacher = 'teacher'
        Student = 'student'
        Marketer = 'marketer'
        Cashier = 'cashier'

    user_type = CharField(max_length=25, choices=Type.choices, default=Type.Student)
    custom_group = ForeignKey('users.CustomGroup', CASCADE, null=True, blank=True)
    branch = ForeignKey('users.Branch', CASCADE, null=True, blank=True)
    phone = PositiveIntegerField(unique=True)
    name = CharField(max_length=255, blank=True)
    balance = FloatField(default=0)

    gender = IntegerField(choices=Gender.choices, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    comment = CharField(max_length=255, null=True, blank=True)
    # "relation_degree": 0,
    photo = ImageField(upload_to='users/photo/', null=True, blank=True)
    datas = JSONField(null=True, blank=True)

    created_by = ForeignKey('users.User', CASCADE, 'created_user', null=True, blank=True)
    updated_by = ForeignKey('users.User', CASCADE, 'updated_user', null=True, blank=True)

    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    addition_contact = JSONField(null=True, blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()


'''
CEO
Branch
Director
Limited
Administrator
Teacher
Student
Marketer
Cashier

'''
