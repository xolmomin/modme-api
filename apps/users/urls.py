from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import CompanyModelViewSet, CourseModelViewSet, BranchModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register('course', CourseModelViewSet, 'course')
router.register('branch', BranchModelViewSet, 'branch')
router.register('company', CompanyModelViewSet, 'company')
router.register('user', UserModelViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
]
