from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField, DateField, \
    BooleanField, PositiveSmallIntegerField

from shared.models import DeletedModel, BaseModel


class Company(BaseModel, DeletedModel):  # Kompaniya
    name = CharField(max_length=255)
    activated_till = DateField(blank=True, null=True)
    logo = ImageField(upload_to='company/logo/', blank=True, null=True)
    about = CharField(max_length=255, null=True, blank=True)
    lead_about = CharField(max_length=255, null=True, blank=True)
    page_background = ImageField(upload_to='subdomain/file/', null=True, blank=True)
    form_background = ImageField(upload_to='subdomain/file/', null=True, blank=True)
    start_of_working_day = PositiveSmallIntegerField(validators=(MaxValueValidator(24), MinValueValidator(0)),
                                                     default=7)
    end_of_working_day = PositiveSmallIntegerField(default=20,
                                                   validators=(MaxValueValidator(24, '24 soat bolishi mumkin'),
                                                               MinValueValidator(0)))


class Branch(BaseModel, DeletedModel):  # Filial
    company = ForeignKey('users.Company', CASCADE)
    name = CharField(max_length=255)
    is_recalculation_on = BooleanField(default=True)


class Role(Model):
    name = CharField(max_length=255)


'''
CEO
Branch
Director
Administrator
Limited
Administrator
Teacher
Student
Marketer
Cashier

'''
