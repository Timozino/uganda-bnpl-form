from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OtherDetailsViewSet
from . import views

router = DefaultRouter()
router.register(r'other-details', OtherDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('additional-info/', views.create_other_details, name='info'),
    path('other-success/', views.other_info, name='other_success'),
]
