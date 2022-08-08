# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from users.models import Course, Room
#
#
# @receiver(post_save, sender=Course)
# def create_room_after_course(sender, **kwargs):
#     data = {
#         'name': 'yangi xona'
#     }
#     Room.objects.create(**data)
#     print(123)
