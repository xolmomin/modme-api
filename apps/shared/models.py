from django.db.models import Model, DateTimeField, BooleanField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeletedModel(Model):
    deleted_at = DateTimeField(null=True, blank=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True
