from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('payments.urls')),
    path('', include('crm.urls')),
]
