from django.contrib import admin

from django.contrib import admin

from users.models import Company, Branch, Course
from users.models.courses import Room


# @admin.register(Branch)
class BranchTabularInline(admin.TabularInline):
    model = Branch
    min_num = 1
    extra = 1
    fields = ['name', 'is_recalculation_on']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    inlines = [BranchTabularInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

'''
superadmin - hamma ishni qiladi
admin      - moderator crud

/admin

moderator  - teacherlar va studentlarni crud
teacher    - oziga tegishli kurslarni koradi va 
ozini kursiga student qoshadi yo ob tashaydi

/moderator


student


'''